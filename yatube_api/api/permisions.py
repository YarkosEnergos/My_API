from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Читать можно всем.
    Изменять/удалять — только владельцу (owner/author).
    """

    def has_object_permission(self, request, view, obj):
        # GET/HEAD/OPTIONS разрешены всем
        if request.method in SAFE_METHODS:
            return True

        # Для изменения/удаления — только автор
        return obj.author == request.user
