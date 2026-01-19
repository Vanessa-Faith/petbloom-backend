from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: str
    name: str

class UserRegister(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: str
    firebaseUid: str
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    country: Optional[str] = None
    profileImage: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    country: Optional[str] = None
    profileImage: Optional[str] = None

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    weight: Optional[float] = None
    description: Optional[str] = None
    images: List[str] = []
    videos: List[str] = []
    healthRecords: Optional[str] = None
    personality: List[str] = []
    breederName: str
    breederRating: float = 5.0
    shelterName: Optional[str] = None
    price: float
    available: bool = True

class PetResponse(PetCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    petType: Optional[str] = None
    brand: Optional[str] = None
    price: float
    images: List[str] = []
    stock: int = 0
    filters: List[str] = []

class ProductResponse(ProductCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class CartItemCreate(BaseModel):
    productId: Optional[str] = None
    petId: Optional[str] = None
    quantity: int = 1

class CartItemResponse(BaseModel):
    id: str
    userId: str
    productId: Optional[str] = None
    petId: Optional[str] = None
    quantity: int
    price: float
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class WishlistCreate(BaseModel):
    productId: Optional[str] = None
    petId: Optional[str] = None

class WishlistResponse(BaseModel):
    id: str
    userId: str
    productId: Optional[str] = None
    petId: Optional[str] = None
    addedAt: datetime

    class Config:
        from_attributes = True

class OrderItemCreate(BaseModel):
    productId: Optional[str] = None
    petId: Optional[str] = None
    quantity: int

class OrderCreate(BaseModel):
    shippingAddress: str
    deliveryOption: str
    pickupLocation: Optional[str] = None

class OrderResponse(BaseModel):
    id: str
    userId: str
    status: str
    totalPrice: float
    shippingAddress: str
    deliveryOption: str
    pickupLocation: Optional[str] = None
    trackingNumber: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class ReviewCreate(BaseModel):
    productId: Optional[str] = None
    petId: Optional[str] = None
    rating: int
    comment: Optional[str] = None

class ReviewResponse(ReviewCreate):
    id: str
    userId: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
