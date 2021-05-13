#!/usr/bin/perl


use CGI qw(:standard escapeHTML);
use DBI;

my $usuario = param('usuario');
my $clave   = param('clave');


my $dsn = "DBI:mysql:host=localhost;database=EIE115";
my $dbh = DBI->connect ($dsn, $usuario, $clave);


print "Content-Type: text/html\n\n";

print<<HEAD;
<!DocType html>
<html>
        <head>
                <title>
                MENU
                </title>
        </head>
        <body>
HEAD
if ($dbh) {

print<<OPCIONES;
1 - CONSULTAR
2 - MODIFICAR
3 - BORRAR
Hugo Miguel Colato Rodriguez20:30
4 - CREAR
Elige una opcion:
<form name="ejecutarOP" action="/cgi-bin/opciones.cgi" method="get">
<input type="text" name="op" length="2">
<input type="submit" value="Seleccionar">
<input type="hidden" value="$usr">

</form>
OPCIONES

$dbh->disconnect ();

} else {

print<<HTML_ERROR;

<b><h1>Credenciales NO Validas!!!</h1></b>


HTML_ERROR
}

print<<FIN;
</body>
</html>
FIN