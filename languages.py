translations = {
    'ar': {
        'welcome': 'أهلاً بك في متجر المنتجات الرقمية!',
        'products': '📦 المنتجات',
        'account': '👤 حسابي',
        'deposit': '💳 شحن الرصيد',
        'support': '🛠 الدعم الفني',
    },
    'en': {
        'welcome': 'Welcome to the digital products store!',
        'products': '📦 Products',
        'account': '👤 My Account',
        'deposit': '💳 Deposit',
        'support': '🛠 Support',
    },
    'ru': {
        'welcome': 'Добро пожаловать в магазин цифровых товаров!',
        'products': '📦 Товары',
        'account': '👤 Аккаунт',
        'deposit': '💳 Пополнить',
        'support': '🛠 Поддержка',
    }
}

def get_text(lang, key):
    return translations.get(lang, translations['ar']).get(key, key)
