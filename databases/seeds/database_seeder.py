"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .product_table_seeder import ProductTableSeeder
from .user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(ProductTableSeeder)