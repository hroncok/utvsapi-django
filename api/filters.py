from rest_framework import filters


class ObjectPermissionsFilter(filters.BaseFilterBackend):
    """
    A filter backend that limits results to those where the requesting user
    has read object level permissions.
    """
    def check_perms(self, view, request, obj):
        try:
            view.check_object_permissions(request, obj)
            return True
        except Exception:
            return False

    def filter_queryset(self, request, queryset, view):
        ids = [o.id for o in queryset if self.check_perms(view, request, o)]
        return queryset.filter(id__in=ids)
