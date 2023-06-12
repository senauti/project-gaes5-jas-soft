<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio Sesion</title>
    <link rel="stylesheet" type="text/css" href="{{ asset('css/login.css') }}">
    <link  rel="shortcut icon" href="{{ asset('pictures/iconlogo.png') }}">
</head>
<body>    
    <header>
        <h2>PROMOPLAST SAS</h2>
        <a href="{{ url('/') }}" class="btn-ingresar"><img class="img-login" src="{{ asset('PICTURES/icons8-atrás-64.png') }}" alt="ingresar"></a>
        <h2>INICIO DE SESION</h2>
    </header>
    <div class="box-content">
        <form  method="POST" action="{{ route('login') }}" class="flex-box needs-validation">
            @csrf
            <img class="imglogin" src="{{ asset('PICTURES/logo.png') }}" alt="Esta imagen no se puede visualizar">
            <div class="row mb-3">
                            <label for="email" class="col-md-4 col-form-label text-md-end">{{ __('Correo') }}</label>

                            <div class="col-md-6">
                                <input id="email" type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ old('email') }}" required autocomplete="email" autofocus>

                                @error('email')
                            <span class="invalid-feedback" role="alert">
                                <strong>El correo ingresado no es correcto o no esta registrado</strong>
                            </span>
                        @enderror
                            </div>
                        </div>
            <div class="row mb-3">
                <label for="password" class="col-md-4 col-form-label text-md-end">{{ __('Contraseña') }}</label>

                    <div class="col-md-6">
                        <input id="password" type="password" class="form-control @error('password') is-invalid @enderror" name="password" required autocomplete="current-password">

                        @error('password')
                            <span class="invalid-feedback" role="alert">
                                <strong>La contraseña es incorrecta</strong>
                            </span>
                        @enderror

                </div>
            </div>
            <div class="row mb-3">
                <div class="col-md-6 offset-md-4">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="remember" id="remember" {{ old('remember') ? 'checked' : '' }}>

                        <label class="form-check-label" for="remember">
                            {{ __('Recordar') }}
                        </label>
                    </div>
                </div>
            </div>
            <div class="row mb-0">
                <div class="col-md-8 offset-md-4">
                    <button type="submit" class="btn btn-primary">
                        {{ __('Ingresar') }}
                    </button>

                    @if (Route::has('password.request'))
                        <a class="btn btn-link" href="{{ route('password.request') }}">
                            {{ __('Recordar contraseña?') }}
                        </a>
                    @endif
                </div>
            </div>
            <a href="{{ url('register') }}">Registrarse</a>
            <a href="">¿Olvidaste tu Contraseña?</a>
        </form>
    </div>
</body> 
</html>