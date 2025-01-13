## Permissions and Groups Setup

### Custom Permissions

The following custom permissions are defined in the `ExampleModel`:

- `can_view`: Can view items
- `can_create`: Can create items
- `can_edit`: Can edit items
- `can_delete`: Can delete items

### Groups

The following groups are set up in the Django admin:

- **Editors**: Permissions: can_edit, can_create
- **Viewers**: Permissions: can_view
- **Admins**: Permissions: can_view, can_create, can_edit, can_delete

### Enforcing Permissions in Views

- Permissions are enforced using the `@permission_required` decorator in views.
- Example views are configured to check for specific permissions before performing actions.
