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

@cli.command()
@click.option('--product_id', prompt='Product ID', help='The ID of the product to delete.', type=int)
def delete_product(product_id):
    """Delete a product by ID."""
    session = Session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
        click.echo(f'Product with ID {product_id} deleted!')
    else:
        click.echo(f'Product with ID {product_id} not found.')
    session.close()

@cli.command()
@click.option('--product_id', prompt='Product ID', help='The ID of the product to update.', type=int)
@click.option('--name', prompt='New Product Name', help='The new name of the product.')
@click.option('--unit', prompt='New Unit', help='New unit of measurement for the product.')
@click.option('--price', prompt='New Price', type=float, help='New price of the product.')
def update_product(product_id, name, unit, price):
    """Update a product by ID."""
    session = Session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        product.name = name
        product.unit = unit
        product.price = price
        session.commit()
        click.echo(f'Product with ID {product_id} updated!')
    else:
        click.echo(f'Product with ID {product_id} not found.')
    session.close()

@cli.command()
@click.option('--user_id', prompt='User ID', help='The ID of the user to delete.', type=int)
def delete_user(user_id):
    """Delete a user by ID."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        click.echo(f'User with ID {user_id} deleted!')
    else:
        click.echo(f'User with ID {user_id} not found.')
    session.close()

@cli.command()
@click.option('--user_id', prompt='User ID', help='The ID of the user to update.', type=int)
@click.option('--name', prompt='New User Name', help='The new name of the user.')
@click.option('--email', prompt='New User Email', help='The new email of the user.')
def update_user(user_id, name, email):
    """Update a user by ID."""
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.email = email
        session.commit()
        click.echo(f'User with ID {user_id} updated!')
    else:
        click.echo(f'User with ID {user_id} not found.')
    session.close()

@cli.command()
def view_orders():
    """View all orders."""
    session = Session()
    orders = session.query(Order).all()
    for order in orders:
        click.echo(f'Order ID: {order.id}, User ID: {order.user_id}, Product ID: {order.product_id}, Quantity: {order.quantity}')
    session.close()

if __name__ == '__main__':
    cli()
