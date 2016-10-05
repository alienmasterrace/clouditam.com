def bar(request):
    return {"bar": 100 * (len(request.user.customer.assets.all()) / request.user.customer.asset_limit)}

