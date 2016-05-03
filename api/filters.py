from rest_framework import filters


class ObjectPermissionsFilter(filters.BaseFilterBackend):
    """
    A filter backend that limits results to those where the requesting user
    has read object level permissions.
    """
    def filter_queryset(self, request, queryset, view):
        if request.auth['_everything']:
            return queryset

        return queryset.filter(personal_number=request.auth['personal_number'])
