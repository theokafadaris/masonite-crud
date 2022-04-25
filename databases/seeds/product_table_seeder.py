"""ProductTableSeeder Seeder."""

from faker import Faker
from masoniteorm.seeds import Seeder
from app.models.Product import Product


class ProductTableSeeder(Seeder):
    def run(self):
        fake=Faker()
        for i in range(5):
            Product.create(
                {
                    "name": "Product {}".format(i),
                    "details": fake.text(),
                }
        )
