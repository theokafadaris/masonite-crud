from email.mime import image
from masonite.request import Request
from masonite.controllers import Controller
from masonite.views import View
from masonite.response import Response
from app.models.Product import Product
from masonite.validation import Validator
from masonite.filesystem import Storage
from masonite.facades import Dump


class ProductController(Controller):
    def index(self, view: View):
        products = Product.all()
        return view.render('products/index', {'products': products})

    def create(self, view: View):
        return view.render('products/create')

    def store(self, storage: Storage, request: Request, response: Response, validate: Validator):

        # Dump.dump(request.input('image'))
        errors = request.validate(
            validate.required(['name', 'details']),
            # validate.file('image', mimes=['pdf', 'txt'])
        )

        if errors:
            return response.redirect('/products/create').with_errors(errors)
        
        path = storage.disk('local').put_file('public', request.input('image'))
        # Dump.dd(str(path))
        Product.create(
            name=request.input('name'),
            details=request.input('details'),
            image = path
        )
        return response.redirect('/products')
    
    def show(self, view: View, request: Request):
        product = Product.where('id', request.param('product_id')).first()
        return view.render('products/show', {'product': product})

    def edit(self, view: View, request: Request):
        product = Product.where('id', request.param('product_id')).first()
        return view.render('products/edit', {'product': product})

    def update(self, request: Request, storage: Storage ,response: Response, validate: Validator):
        errors = request.validate(
            validate.required(['name', 'details']),
        )

        if errors:
            return response.redirect('/products/edit/{}'.format(request.input('id'))).with_errors(errors)
        product = Product.where('id', request.input('id')).first()
        if request.input('image').name:
            path = storage.disk('local').put_file('public', request.input('image'))
            product.image = path
        product.name = request.input('name')
        product.details = request.input('details')
        product.save()
        return response.redirect('/products')

    def delete(self, request: Request, response: Response):
        product = Product.where('id', request.param('product_id')).first()
        product.delete()
        return response.redirect('/products')
