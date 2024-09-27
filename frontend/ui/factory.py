from typing import Callable

from frontend.ui.configure_company_view import company_view
from frontend.ui.configure_strong_entities_view import strong_entities_view
from frontend.ui.configure_weak_entities_view import weak_entities_view
from frontend.ui.employee_view import employee_view
from frontend.utils.enum import ViewEnum

FACTORY = {
    ViewEnum.company_view.value: company_view,
    ViewEnum.employee_view.value: employee_view,
    ViewEnum.strong_entities_view.value: strong_entities_view,
    ViewEnum.weak_entities_view.value: weak_entities_view,
}


class ViewFactory:

    @staticmethod
    def get_view(view_name: str) -> Callable:
        if view_name in FACTORY:
            provider_class = FACTORY[view_name]
            return provider_class
        else:
            raise ValueError(f"This embedding provider '{view_name}' is not supported.")
