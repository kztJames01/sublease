
declare interface AuthenticationProps{
    type: 'signup' | 'login' | 'logout' | 'password_reset'
}

declare type NewUserParams = {
    username: string;
    email: string;
    password: string;
}

declare type LoginUserParams = {
    username: string;
    password: string;
}

declare type SearchParamsProps = {
    params: { [key: string]: string},
    searchParams: { [key: string]: string}
}



