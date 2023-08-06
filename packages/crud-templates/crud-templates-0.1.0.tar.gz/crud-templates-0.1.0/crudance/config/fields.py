class PostInputFields:
    """Generic fields for POST input or output."""
    fields = "fields"
    filters = "filters"
    order_by = "order_by"
    limit = "limit"
    offset = "offset"
    operator_choice = "operator_choice"

    class Operators:
        """Authorized boolean operators for filters."""
        and_ = "and"
        or_ = "or"
