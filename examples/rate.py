"""Give a 5-star rating to 20 lucky 24-year-old straight/gay/bi women/men."""

import okcupyd

u = okcupyd.User()
profiles = u.search(location='minneapolis, mn', keywords='arrested development',
                    age_min=24, age_max=24, number=20)
for profile in profiles:
    profile.rate(5)
