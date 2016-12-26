from django.conf import settings


def settings_context_processor(request):
    setting_dict = {
        "FEES_UNPAID_STATUS": settings.FEES_UNPAID_STATUS,
        "FEES_PAID_STATUS": settings.FEES_PAID_STATUS
    }

    return setting_dict