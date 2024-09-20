import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Product, Order, Base

# Create a database engine
DATABASE_URI = 'postgresql://abdalla:Rayan101@localhost/grocery_shop'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Grocery Shop Management System CLI."""
    pass

@cli.command()
@click.option('--name', prompt='Product name', help='The name of the product.')
@click.option('--unit', prompt='Unit', help='The unit of the product (e.g., kg, lb).')
@click.option('--price', prompt='Price', type=float, help='The price of the product.')
def add_product(name, unit, price):
    """Add a new product."""
    session = Session()
    product = Product(name=name, unit=unit, price=price)
    session.add(product)
    session.commit()
    click.echo(f'Product {name} added!')

@cli.command()
@click.option('--name', prompt='User name', help='The name of the user.')
@click.option('--email', prompt='User email', help='The email of the user.')
def add_user(name, email):
    """Add a new user."""
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    click.echo(f'User {name} added!')

@cli.command()
def list_products():
    """List all products."""
    session = Session()
    products = session.query(Product).all()
    for product in products:
        click.echo(f'ID: {product.id}, Name: {product.name}, Unit: {product.unit}, Price: {product.price}')

@cli.command()
def list_users():
    """List all users."""
    session = Session()
    users = session.query(User).all()
    for user in users:
        click.echo(f'ID: {user.id}, Name: {user.name}, Email: {user.email}')

@cli.command()
@click.option('--user_id', prompt='User ID', help='The ID of the user placing the order.', type=int)
@click.option('--product_id', prompt='Product ID', help='The ID of the product to order.', type=int)
@click.option('--quantity', prompt='Quantity', help='The quantity of the product.', type=int)
def place_order(user_id, product_id, quantity):
    """Place a new order."""
    session = Session()
    order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    session.add(order)
    session.commit()
    click.echo(f'Order placed for User ID {user_id} with Product ID {product_id}.')

if __name__ == '__main__':
    cli()
