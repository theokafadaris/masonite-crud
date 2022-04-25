from masonite.request import Request
from masonite.controllers import Controller
from masonite.views import View
from masonite.response import Response
from app.models.Product import Product
from masonite.validation import Validator


class ProductController(Controller):
    def index(self, view: View):
        products = Product.all()
        return view.render('products/index', {'products': products})

    def create(self, view: View):
        return view.render('products/create')

    def store(self, request: Request, response: Response, validate: Validator):
        errors = request.validate(
            validate.required(['name', 'details']),
        )

        if errors:
            return response.redirect('/products/create').with_errors(errors)
        Product.create(
            name=request.input('name'),
            details=request.input('details')
        )
        response.redirect('/products')
    
    def show(self, view: View, request: Request):
        product = Product.where('id', request.param('product_id')).first()
        return view.render('products/show', {'product': product})

    def edit(self, view: View, request: Request):
        product = Product.where('id', request.param('product_id')).first()
        return view.render('products/edit', {'product': product})

    def update(self, request: Request, response: Response, validate: Validator):
        errors = request.validate(
            validate.required(['name', 'details']),
        )

        if errors:
            return response.redirect('/products/edit/{}'.format(request.input('id'))).with_errors(errors)
        product = Product.where('id', request.input('id')).first()
        product.name = request.input('name')
        product.details = request.input('details')
        product.save()
        response.redirect('/products/edit/{}'.format(request.input('id')))

    def delete(self, request: Request, response: Response):
        product = Product.where('id', request.param('product_id')).first()
        product.delete()
        response.redirect('/products')
