from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.application.use_cases.auth.authenticate_user_use_case import (
    AuthenticateUserUseCase,
)
from src.application.use_cases.auth.get_current_user_use_case import GetCurrentUserUseCase
from src.application.use_cases.user.create_user_use_case import CreateUserUseCase
from src.domain.schemas import Token, User, UserCreate
from src.infrastructure.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.infrastructure.database.manager import UnitOfWork

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=User)
def register(user: UserCreate, uow: UnitOfWork = Depends(UnitOfWork)):
    with uow.get_session() as session:
        use_case = CreateUserUseCase(session)
        return use_case.execute(user)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    with uow.get_session() as session:
        use_case = AuthenticateUserUseCase(session)
        user = use_case.execute(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
def read_users_me(token: str = Depends(oauth2_scheme), uow: UnitOfWork = Depends(UnitOfWork)):
    with uow.get_session() as session:
        use_case = GetCurrentUserUseCase(session)
        user = use_case.execute(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
