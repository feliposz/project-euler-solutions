program euler10;

uses
   math;

function primo(n : longint) : boolean;
var
r, f : longint;
res : boolean;
begin
   if n = 1 then
      primo := false
   else if n < 4 then
      primo := true  { 2 e 3 sao primos}
   else if (n mod 2) = 0 then
      primo := false
   else if n < 9 then
      primo := true  { ja foi excluido 4, 6 e 8}
   else if (n mod 3) = 0 then
      primo := false
   else
   begin
      r := floor(sqrt(n));  { r * r <= n}
      f := 5;
      primo := true;
      while (f <= r) and primo do
      begin
        if (n mod f = 0) then
           primo := false
        else if (n mod (f + 2)) = 0 then
           primo := false;
        f := f + 6;
      end;
   end;
end;

var
   num: longint;
   soma: int64;

begin
   num := 1;
   soma := 2; {j  soma o 2! }
   while num < 2000000 do
   begin
      num := num + 2;
      write(num, #9);
      if primo(num) then begin
         soma := soma + num;
      end;
   end;
   writeln;
   writeln('A soma dos primos abaixo de 2 mi ‚: ', soma);
   readln;
end.
