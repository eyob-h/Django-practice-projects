
def detectUser(user):
    print(f"00000000002222222222222000000000000 {user.get_role()}")

    if user.get_role() == 'Vendor':
        redirectURL = 'venDashboard'
        return redirectURL
    elif user.get_role() == 'Customer':
        redirectURL = 'custDashboard'
        return redirectURL