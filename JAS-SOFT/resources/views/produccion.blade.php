<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   

    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Style.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Header.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/footer.css') }}">
    <link rel="stylesheet" href="{{ asset ('css/estilos-dash-admin.css') }}"> 
    
    <link href="{{ asset ('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css') }}" rel="stylesheet"> 
    
    <link rel="stylesheet" href="{{ asset('https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css')}}">  


    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <link  rel="shortcut icon" href="PICTURES/iconlogo.png">

    <link  rel="shortcut icon" href="PICTURES/iconlogo.png">
    <title>PromoPlast | Produccion</title>
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
        </ul>        
      </div>

    <div class="col-10" id="contentd">
        <div class="card" id="cardash">
          <nav class="descrip-menu">
          <a class="message-ubication" href="{{ url('insumos') }}">Insumos</a>        
          </nav> 
          <div class="container mt-3">
            <h2>PRODUCCION</h2>
            <p></p>      
            <table class="table table-striped" id="tablas">
              <thead>
                <tr>
                  <th>Codigo produccion</th>
                  <th>Nombre</th>
                  <th>Estado</th>
                  <th>Cantidad</th>   
                  <th>Operario</th>   
                  <th>Fecha</th>
                  <th>Cod Insumo</th>   
                  <th></th>       
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>10019381</td>
                  <td>Tappers</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>200</td>
                  <td>pepito perez</td>
                  <td>23/03/2023</td>
                  <td>20019392</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019382</td>
                  <td>jarra 1.5L plastico</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>700</td>
                  <td>Santiago</td>
                  <td>23/03/2023</td>
                  <td>20019372</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Baby bowl</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>40</td>
                  <td>juanito</td>
                  <td>20/03/2023</td>
                  <td>20019383</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>10</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>100</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>70</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>300</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Tappers</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>700</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019392</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>10</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>80</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
                <tr>
                  <td>10019383</td>
                  <td>Ganchos autoadesivos</td>
                  <td><select class="form-select" aria-label="Default select example" id="select1">
                    <option selected>Estados</option>
                    <option value="1">Espera</option>
                    <option value="2">produccion</option>
                    <option value="3">Finalizado</option>
                  </select></td>
                  <td>240</td>
                  <td>juanito</td>
                  <td>23/03/2023</td>
                  <td>20019381</td>
                  <td>
                    <img src="PICTURES/icons-editar.png" alt="editar" width="20px">
                    <img src="PICTURES/icons-basura.png" alt="eliminar" width="20px">
                  </td>
                </tr>
              </tbody>
            </table>     
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
              Agregar Produccion
            </button>
                        
            <!-- The Modal -->
            
          </div>           
        </div>    
    </div>    
  </body>

<<<<<<< Updated upstream
    <script src="jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="{{ asset ('js/jquery.dataTables.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset ('js/dataTables.bootstrap.min.js') }}"></script>
    <script src="{{ asset ('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js') }}"></script>
    <script src="{{ asset ('https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js') }}"></script>
      <script type="text/javascript" src="{{ asset ('js/validaciones.js') }}"></script>
      <script src="JS/slidebar.js"></script>
        
      <script>
        $(document).ready( function () {
=======
            <div class="col-10" id="contentd">
                <div class="card" id="cardash">
                    <nav class="descrip-menu">
                        <a class="message-ubication" href="{{ url('insumos') }}">Insumos</a>
                    </nav>
                    <div class="container mt-3">
                        <h2>PRODUCCION</h2>
                        <p></p>
                        <table class="table table-striped" id="tablas">
                            <thead>
                                <tr>
                                    <th>Codigo produccion</th>
                                    <th>Cantidadproducto</th>
                                    <th>Fechapedido</th>
                                    <th>Idproducto</th>
                                    <th>Idestadopedido</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>

                                @foreach ($ordenpedidos as $ordenpedido)
                                    <tr>
                                        <td>{{ $ordenpedido->IdOrdenPedido }}</td>
                                        <td>{{ $ordenpedido->cantidadProducto }}</td>
                                        <td>{{ $ordenpedido->fechaPedido }}</td>
                                        <td>{{ $ordenpedido->IdProducto }}</td>
                                        <td>{{ $ordenpedido->IdEstadopedido }}</td>

                                        <td>
                                            <form action="{{ route('ordenpedido.eliminar', $ordenpedido->id) }}"
                                                method="POST">
                                                <a class="btn btn-sm btn-success"
                                                    href="{{ route('ordenpedido.edit', $ordenpedido->id) }}"><i
                                                        class="fa fa-fw fa-edit"></i> {{ __('Editar') }}</a>
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="btn btn-danger btn-sm"><i
                                                        class="fa fa-fw fa-trash"></i> {{ __('Eliminar') }}</button>
                                            </form>
                                        </td>
                                    </tr>
                                @endforeach
                            </tbody>
                        </table>
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
                            Agregar Produccion
                        </button>                       
                    </div>
                </div>
            </div>
</body>

<script src="jquery-3.6.0.min.js"></script>
<script type="text/javascript" src="{{ asset('js/jquery.dataTables.min.js') }}"></script>
<script type="text/javascript" src="{{ asset('js/dataTables.bootstrap.min.js') }}"></script>
<script src="{{ asset('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js') }}"></script>
<script src="{{ asset('https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js') }}"></script>
<script type="text/javascript" src="{{ asset('js/validaciones.js') }}"></script>
<script src="JS/slidebar.js"></script>

<script>
    $(document).ready(function() {
>>>>>>> Stashed changes
        $('#tablas').DataTable();
        } );

        function soloLetras(e) {
          var key = e.keyCode || e.which,
            tecla = String.fromCharCode(key).toLowerCase(),
            letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
            especiales = [8, 37, 39, 46],
            tecla_especial = false;
      
          for (var i in especiales) {
            if (key == especiales[i]) {
              tecla_especial = true;
              break;
            }
          }
      
          if (letras.indexOf(tecla) == -1 && !tecla_especial) {
            return false;
          }
        }
      </script>  
      

    
</html>