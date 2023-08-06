from marshmallow import Schema, fields as mshm_fields
from marshmallow.validate import OneOf, Length


AUTHORIZED_OPERATORS = ("and", "or")


class PostInputSchema(Schema):
    """Generic input schema for POST endpoints.

    All fields can be rewritten in the inherited schema, filters in particular that
    should be rewritten with a nested schema. ``fields`` and ``order_by`` can be
    limited to certain values using a validation with ``OneOf``.
    """
    class RangeFilterSchema(Schema):
        """Schema for range (number or date) filters.

        Note that dates will be converted by the filtering method, so string types
        work for both dates and numbers here.
        """
        lower_bound = mshm_fields.String(required=False)
        upper_bound = mshm_fields.String(required=False)

    class OrderBySpecificationSchema(Schema):
        """Schema for order by fields."""
        field = mshm_fields.String(required=True)
        direction = mshm_fields.String(required=False, load_default="asc", validate=OneOf(("desc", "asc")))

    filters = mshm_fields.Dict(required=True)  # Rewrite this field with the nested schema of desired Filters
    fields = mshm_fields.List(mshm_fields.String, validate=Length(min=1), required=True)
    offset = mshm_fields.Integer(required=False)
    limit = mshm_fields.Integer(required=False)
    order_by = mshm_fields.List(mshm_fields.Nested(OrderBySpecificationSchema), required=False)
    operator_choice = mshm_fields.String(validate=OneOf(AUTHORIZED_OPERATORS), required=False)


class PostOutputSchema(Schema):
    """Generic output schema for POST endpoints.

    ``pagination`` field can be left as such, ``data`` must be rewritten in the
    inherited schema with the schema of output entities.
    """
    class Pagination(Schema):
        """Pagination schema."""
        total_item_count = mshm_fields.Integer(required=True)
        total_page_count = mshm_fields.Integer(required=True)

    data = mshm_fields.List(mshm_fields.Dict(), required=True)  # Rewrite data field with the entities schema
    pagination = mshm_fields.Nested(Pagination, required=True)
