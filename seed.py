import asyncio
from prisma import Prisma

async def seed():
    prisma = Prisma()
    await prisma.connect()
    
    pets_data = [
        {"name": "Max", "species": "dogs", "breed": "Golden Retriever", "age": 2, "weight": 30, "description": "Friendly and energetic golden retriever", "images": ["https://images.unsplash.com/photo-1633722715463-d30f4f325e24?w=400"], "videos": [], "personality": ["friendly", "energetic"], "breederName": "Golden Dreams", "breederRating": 4.8, "price": 1200.00, "available": True},
        {"name": "Whiskers", "species": "cats", "breed": "Persian", "age": 1, "weight": 4.5, "description": "Elegant Persian cat", "images": ["https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?w=400"], "videos": [], "personality": ["calm", "affectionate"], "breederName": "Purrfect Cats", "breederRating": 4.9, "price": 800.00, "available": True},
        {"name": "Buddy", "species": "dogs", "breed": "Labrador", "age": 3, "weight": 35, "description": "Playful Labrador", "images": ["https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400"], "videos": [], "personality": ["playful", "loyal"], "breederName": "Happy Paws", "breederRating": 4.7, "price": 1000.00, "available": True}
    ]
    
    products_data = [
        {"name": "Premium Dog Food", "description": "Nutritious dry dog food", "category": "food", "petType": "dogs", "brand": "PetPro", "price": 45.99, "images": ["https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=400"], "stock": 50, "filters": ["adult"]},
        {"name": "Cat Bed", "description": "Comfortable cat bed", "category": "habitats", "petType": "cats", "brand": "CatsLounge", "price": 65.00, "images": ["https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?w=400"], "stock": 25, "filters": ["comfortable"]},
        {"name": "Dog Toy Set", "description": "Set of 5 interactive toys", "category": "toys", "petType": "dogs", "brand": "PlayPets", "price": 29.99, "images": ["https://images.unsplash.com/photo-1591769225440-811ad7d6eab3?w=400"], "stock": 40, "filters": ["durable"]}
    ]
    
    for pet in pets_data:
        await prisma.pet.create(data=pet)
    
    for product in products_data:
        await prisma.product.create(data=product)
    
    print("✅ Database seeded successfully!")
    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(seed())
