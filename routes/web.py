from masonite.routes import Route

ROUTES = [Route.get("/", "ProductController@index"),
          Route.get("/products", "ProductController@index"),
          Route.get("/products/create", "ProductController@create"),
          Route.post("/products", "ProductController@store"),
          Route.get("/products/show/@product_id", "ProductController@show"),
          Route.get("/products/edit/@product_id", "ProductController@edit"),
          Route.post("/products/update", "ProductController@update"),
          Route.get('/products/delete/@product_id', 'ProductController@delete'),
          ]
