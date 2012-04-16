{
An adapted version of http://mathworld.wolfram.com/Stern-BrocotTree.html
Inspired by Pier(Pascal) post at http://projecteuler.net/thread=73
Had to set Stack size = 60000000

This took 1 hour and 7 minutes to run aprox.
}

Var
  n: longint;
  r: int64;

Procedure arbol (n1,d1,n2,d2: longint);
var
  an,ad: longint;
begin
  an:= n1+n2; ad:= d1+d2;
  if (an <= ad) then
  begin
    if (ad+d1 <= n) then arbol (n1, d1, an, ad);
    Inc(r);
    if (ad+d2 <= n) then arbol (an, ad, n2, d2);
  end;
end;

Begin
     n:= 1000000;
     arbol (0,1,1,0);
     writeln(r-1); readln; {why -1 if n > 10 ???}
End.
