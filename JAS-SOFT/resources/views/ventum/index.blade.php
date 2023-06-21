<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Style.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Header.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/footer.css') }}">

    <link href="{{ asset ('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css') }}" rel="stylesheet">
    <link rel="stylesheet" href="{{ asset ('css/estilos-dash-admin.css') }}">
    <link rel="stylesheet" href="{{ asset ('css/jquery.dataTables.min.css') }}">
    <script src="{{ asset ('js/bootstrap.bundle.min.js') }}"></script>

    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <link rel="shortcut icon" href="PICTURES/iconlogo.png">
    <title>PromoPlast | Ventas</title>
</head>

<body>
    <header class="dash-menu">
        <img class="logo-dash-admin" src="PICTURES/logo.png" alt="logo">
        <a class="nav-link" href="{{ url('/index') }}">INICIO</a>
        <ul class="list-menu-ul">
            <li class="list-menu-dash"> <img class="img-menu-dash" src="PICTURES/campana.png" alt="Campana"> </li>
            <li class="list-menu-dash"> Administrador (Administrador) </li>
            <li class="list-menu-dash"> <img class="img-menu-dash rotate-img" src="PICTURES/flecha.png" alt="flecha"> </li>
            <li class="list-menu-dash"> <img class="img-menu-dash-users" src="PICTURES/usuario.png" alt=""> </li>
        </ul>
    </header>

    <div class="container-fluid">
        <div class="row">
            <div class="col-2 barmenu">
                <h3 class="mt-4">PROMOPLAST</h3>
                <p></p>
                <ul class="nav nav-pills flex-column">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/dashboard') }}">MENU</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/rrhh') }}">RRHH</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/produccion') }}">PRODUCCION</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/inventario') }}">INVENTARIO</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/ventas') }}">VENTAS</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url('/buzon') }}">BUZON</a>
                    </li>
                </ul>
            </div>

            <div class="col-10" id="contentd">
                <div class="card" id="cardash">
                    <div class="container mt-3">
                        <h2>VENTAS</h2>
                        <p></p>
                        <div class="tarjetas">
                            <div class="row">
                                <div class="col">
                                    <img src="PICTURES/grafico1.png" alt="grafico1" id="grafico">
                                </div>
                                <div class="col">
                                    <img src="PICTURES/grafico2.png" alt="grafico2" id="grafico">
                                </div>
                            </div>
                        </div>
                        <table class="table table-striped" id="tablas">
                            <thead class="thead">
                                <tr>
                                    <th>Idventa</th>
                                    <th>Fecha</th>
                                    <th>Total</th>
                                    <th>Subtotal</th>
                                    <th>Descuento</th>
                                    <th>IVA</th>
                                    <th>Cliente</th>
                                    <th>Pagos</th>
                                    <th>Empleado</th>
                                    <th>Ordenpedido</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                @foreach ($ventas as $venta)
                                <tr>
                                    <td>{{ $venta->IdVenta }}</td>
                                    <td>{{ $venta->fecha }}</td>
                                    <td>{{ $venta->totalVenta }}</td>
                                    <td>{{ $venta->subTotal }}</td>
                                    <td>{{ $venta->CantidadDescuento }}</td>
                                    <td>{{ $venta->totalIva }}</td>
                                    <td>{{ $venta->IdCliente }}</td>
                                    <td>{{ $venta->IdPagos }}</td>
                                    <td>{{ $venta->IdEmpleado }}</td>
                                    <td>{{ $venta->IdOrdenPedido }}</td>
                                    <td>
                                        <form action="{{ route('ventum.eliminar', $venta->IdVenta) }}" method="POST">
                                            <a class="btn btn-sm btn-success" href="{{ route('ventum.edit', $venta->IdVenta) }}"><i class="fa fa-fw fa-edit"></i> {{ __('Edit') }}</a>
                                            @csrf
                                            <button type="submit" class="btn btn-danger btn-sm"><i class="fa fa-fw fa-trash"></i> {{ __('Delete') }}</button>
                                        </form>
                                    </td>
                                </tr>
                                @endforeach
                            </tbody>
                        </table>
                        @include ('ventum.create')
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
                            Nueva venta
                        </button>

                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script type="text/javascript" src="{{ asset('JS/jquery.dataTables.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset('JS/dataTables.bootstrap.min.js') }}"></script>
    <script>
        $(document).ready(function() {
            $('#tablas').DataTable();
        });

        function mostrarid() {
            id = document.getElementById('idventa').value;
            alert(id);
        }

        function abrirmodal() {
            $('#editar').show();
        }
    </script>
</body>

</html>
