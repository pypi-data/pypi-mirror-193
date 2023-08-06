"""
    This `locations` part of the library will allow you to analyze and
    make interesting statistics about the whole collection of locations
    you might have on your target.

    The main function in `estimate()`. Turn your latitude-longitude
    locations to a list of `HashablePoint` objects, and input it in
    the `estimate()` function, you will obtain the list of main locations
    of your target.
"""
from geopy import distance, point

__all__ = "HashablePoint", "LocationGuesser", "LocationGuessingResult"
default_km_radius = 20

class HashablePoint(point.Point):
    """
        The `HashablePoint` object is an object pointing at a location.
        It's two arguments are `latitude` and `longitude`.
    """
    def __new__(cls, latitude=None, longitude=None, _ignored_altitude=None):
        return super().__new__(cls, latitude, longitude, 0)

    def __hash__(self) -> int:
        return hash(repr(self))

    def __sub__(self, other: point.Point) -> "HashablePoint":
        assert isinstance(other, point.Point)
        return HashablePoint(
            sum([self.latitude, other.latitude]) / 2,
            sum([self.longitude, other.longitude]) / 2
        )

PointToFloat = dict[HashablePoint, float]
IntersectionnedPoints = dict[HashablePoint, PointToFloat]

def score(distance: float | int, radius: int = default_km_radius) -> float:
    """
        Makes the score of proximity based on the km `distance` (`float`
        or `int`), based on the radius `radius` (`int`). The result will
        be a `float` bewteen 0 and 1.
    """
    if distance > radius:
        return 0.0
    elif distance:
        return ((radius - distance) / distance) / radius
    else:
        return 1.0

def point_spaces(points: list[HashablePoint]) -> IntersectionnedPoints:
    """
        Returns a dictionnary, in which avery key is a `HashablePoint`
        (parent key) from the argument `points` (being a `list` of
        `HashablePoint`), and each value is a `dict`, in which avery key
        is also some `HashablePoint` objects (child key), pointing the
        `float` values of the distance in km between the parent key and
        the child key. As an example:
        >>> #         pA                  pB                  pC
        >>> points = [HashablePoint(), HashablePoint(), HashablePoint()]
        >>> # Result of `point_spaces`:
        >>> point_spaces(points)
        {
            pA: {
                pB: float(pA2B), # Km distance bewteen pA and pB
                pC: float(PA2C), # Km distance bewteen pA and pC
            },
            pB: {
                pB: float(pB2A), # Km distance bewteen pB and pA
                pC: float(PB2C), # Km distance bewteen pB and pC
            },
            pC: {
                pB: float(pC2A, # Km distance bewteen pC and pA
                pC: float(PB2B), # Km distance bewteen pC and pB
            },
        }
    """
    # We make a dictionnary. Each of its keys is a `HashablePoint`
    # object, and each of its values are also dict, whose keys are also
    # `HashablePoint`, and the values are the distance score bewteen the
    # parent key, and the current key. Long story short, it is a dict of
    # the distance scores between each points.
    result = {}
    for point_index, point in enumerate(points):
        result[point] = {
            compared_point: distance.distance(point, compared_point).km
            for cp_index, compared_point in enumerate(points)
            if cp_index != point_index
        }
    return result

def score_point_spaces(
    points: list[HashablePoint],
    radius: int | float = default_km_radius,
    keep_0_scores: bool = False,
    remove_isolated: bool = False
) -> IntersectionnedPoints:
    """
        Turns distances of the `point_spaces(...)` result to a score,
        a `float` bewteen `0.0` and `1.0`. Higher the score is, higher
        is the probability these locations are linked.
        - `points` must be a `list` of `HashablePoint`.
        - `radius` is the distance in km over which you consider two
            points as not linked. Default is `20`.
        - `keep_0_scores` on `True` will remove from the score the key
            value pair that has scores `0.0`. Default on `True`.
        - `remove_isolated` on `True` will remove points that has no
            links to others. Default on `False`.
        
        The result is the edited value of argument `points`.
    """
    # Here, for each point; we are removing its distances score that are
    # under 0, so each points only keeps the points related to itself.
    results: IntersectionnedPoints = {}
    for point, values in point_spaces(points).items():
        result: PointToFloat = {}
        for value_point, distance in values.items():
            if (_score := score(distance, radius=radius)) > 0 or keep_0_scores:
                result[value_point] = _score
        results[point] = result

    # If `remove_isolated` is `True`, we are removing all the points that
    # are not linked to any other points.
    if remove_isolated and not keep_0_scores:
        results = { point: values for point, values in
                    results.items() if any(values.values()) }

    return results

def locations_to_groups(
    locations: IntersectionnedPoints
) -> list[list[HashablePoint]]:
    """
        Turns the locations of arg `locations` to a `list` of `list` of
        `HashablePoint`. These lists are groups of locations, that have
        been placed with others because of their geographical proximity.
        - `locations` must be the result of `score_point_spaces(...)`,
            preferably without touching its `keep_0_scores` argument.
    """
    groups: list[list[HashablePoint]] = []
    for base_point, values in locations.items():
        matching_groups: list[int] = []

        # Here we enumerate the locations that has, from the `base_point`,
        # a score higher than 0 (because we filtered them at the previous
        # step), and if one of the enumerated locations is already in an
        # other existing group, we append to `matching_groups` the index
        # of this existing group. Likeso, we can have many groups being
        # far from each others, but having location in between them that
        # are linking them.
        for group_index, group in enumerate(groups):
            if any([okay_distance in group for okay_distance in values.keys()]):
                matching_groups.append(group_index)

        # Here, if we have many distant groups indexes, that means these
        # groups were linked by a location between them. So we remove them
        # individually of `groups`, then compile them and making sure
        # there are not duplicates, and we add the result to `groups`.
        if len(matching_groups) > 1:
            grouped_points = []
            for group_index in sorted(matching_groups, reverse=True):
                grouped_points += groups.pop(group_index)
            groups.append(list(set(grouped_points)))

        # However, if there's only one group matching, we append our point
        # to it.
        elif matching_groups:
            groups[matching_groups[0]].append(base_point)

        # And if there's no group at all, we create it.
        else:
            groups.append([base_point])
    return groups

def group_location(
    group: list[HashablePoint],
    weight: bool = True
) -> HashablePoint:
    """
        Returns the estimated center of a group `group` of locations.
        `group` must be a `list` of `HashablePoint`. The result is a
        `HashablePoint` object.
    """
    inters_points = point_spaces(group)
    # `closest_points` is a list of segments, as:
    # `{START_POINT: [STOP_POINT, SCORE], ...}`
    closest_points = { point: min(value.items(), key=lambda items: items[1])
                        for point, value in inters_points.items() }
    closest_points = dict(sorted(
        closest_points.items(),
        key=lambda items: items[1][1],
        reverse=True
    ))
    closest_points = dict(closest_points)

    latitudes : list[float] = []
    longitudes: list[float] = []

    for index, (point_a, (point_b, distance)) in enumerate(closest_points.items()):
        point_c = point_a - point_b
        # Since the index is the lowest for the most spaced locations, the
        # the greatest for the closest locations, we are placing `index`
        # times the coordinates to the final result, so the closest locations
        # have a grater impact than the one very far, that would make this
        # problem when making averages:
        # You can have 99 times 1, and 1 times 100000, you will get 1001, while
        # 99% of the numbers are 1.
        for x in range(int(index)):
            latitudes.append(point_c.latitude)
            longitudes.append(point_c.longitude)
            if not weight:
                break
    else:
        return HashablePoint(
            sum(latitudes) / len(latitudes),
            sum(longitudes) / len(longitudes)
        )

def estimate(
    locations: list[HashablePoint],
    radius: int = default_km_radius,
    remove_isolated: bool = False,
    weight_in_groups: bool = True
) -> list[tuple[HashablePoint, float]]:
    """
        Estimates centers of the locations.
        - `locations` must be the `list` of your locations as `HashablePoint`
            objects.
        - `radius` is the distance in km over which we consider two points
            aren't linked at all.
        - `remove_isolated` on `True` will not remove groups that contains
            only one item.

        The result will be a `list` of `tuple`. Each of these them are a
        group of locations (they were grouped because of their geographic
        proximity). The first item of the `tuple` is a `HashablePoint`
        object, poiting to the location that have been estimated as the
        central location of the group. The second item of the tuple is the
        `int` amount of locations present in the group. Ex:
        >>> [
        >>>     (Group1HashablePoint, amount_of_locations_in_it),
        >>>     (Group2HashablePoint, amount_of_locations_in_it),
        >>>     ...
        >>> ]
    """
    inters_points = score_point_spaces(locations, radius, remove_isolated)

    # We will split the list of locations in many groups, so we can see
    # the principal different locations of the target.
    groups = locations_to_groups(locations=inters_points)

    results = []
    for group in groups:
        result = group_location(group, weight_in_groups) if len(group) > 1 else group[0]
        results.append((result, len(group)))

    return results

del (default_km_radius, PointToFloat, IntersectionnedPoints)