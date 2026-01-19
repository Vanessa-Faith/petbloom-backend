from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import PetResponse, PetCreate
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/species/list")
async def get_species_list():
    try:
        pets = await prisma_client.pet.find_many(select={"species": True})
        species = list(set([pet.species for pet in pets]))
        return species
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/breeds/{species}")
async def get_breeds_by_species(species: str):
    try:
        pets = await prisma_client.pet.find_many(where={"species": species}, select={"breed": True})
        breeds = list(set([pet.breed for pet in pets]))
        return breeds
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("")
async def get_pets(skip: int = 0, limit: int = 20, species: str = None, available: bool = True):
    try:
        where_clause = {"available": available}
        if species:
            where_clause["species"] = species
        
        pets = await prisma_client.pet.find_many(where=where_clause, skip=skip, take=limit, order={"createdAt": "desc"})
        total = await prisma_client.pet.count(where=where_clause)
        
        return {"data": pets, "total": total}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(pet_id: str):
    try:
        pet = await prisma_client.pet.find_unique(where={"id": pet_id})
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return pet
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=PetResponse)
async def create_pet(pet: PetCreate):
    try:
        new_pet = await prisma_client.pet.create(data=pet.dict())
        return new_pet
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{pet_id}", response_model=PetResponse)
async def update_pet(pet_id: str, pet_update: PetCreate):
    try:
        updated_pet = await prisma_client.pet.update(where={"id": pet_id}, data=pet_update.dict())
        return updated_pet
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{pet_id}")
async def delete_pet(pet_id: str):
    try:
        await prisma_client.pet.delete(where={"id": pet_id})
        return {"message": "Pet deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
