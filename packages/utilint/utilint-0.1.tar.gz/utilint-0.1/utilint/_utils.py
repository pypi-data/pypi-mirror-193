import functools

def saved_result(
    func=None, /, *,
    custom_field: str = None,
    disable_save_result_key: str = "_save_result",
    disable_save_result_attr: str = "_save_results"
):
    """
        This decorator will save the result of the decorated
        function, and will return its saved result whenever
        called again. This saves time.
    """
    if func is None:
        return functools.partial(saved_result, custom_field=custom_field)
    
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        field_name = custom_field or f"_{func.__name__}"

        if disable_save_result_key in kwargs:
            save_result = bool(kwargs[disable_save_result_key])
        elif hasattr(self, disable_save_result_attr):
            save_result = bool(getattr(self, disable_save_result_attr))
        else:
            save_result = True

        try:
            value = getattr(self, field_name)
            if value is None:
                raise AttributeError()
            else:
                return value
        except AttributeError:
            result = func(self, *args, **kwargs)
            if save_result:
                setattr(self, field_name, result)
            return result
    
    return wrapper