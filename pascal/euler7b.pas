program euler7;
{ Funcao : Implementacao do metodo descrito no site do Project Euler}
{ Autor : Felipo}
{ Data : 25/03/2012}

{ If a good upper bound for the target prime is known in advance
 using}
{ a sieve of Eratosthenes is a much more efficient method.}

{ Some useful facts:}
{ 1 is not a prime.}
{ All primes except 2 are odd.}
{ All primes greater than 3 can be written in the form  6k+/-1.}
{ Any number n can have only one primefactor greater than n .}
{ The consequence for primality testing of a number n is:}
{   if we cannot find a number f less than}
{   or equal sqrt(n) that divides n then n is prime:}
{   the only primefactor of n is n itself}


uses
   math;

function primo(n : longint) : boolean;
var
r
 f : longint;
res : boolean;
begin
   if n = 1 then
      primo := false
   else if n < 4 then
      primo := true  { 2 e 3 sao primos}
   else if (n mod 2) = 0 then
      primo := false
   else if n < 9 then
      primo := true  { ja foi excluido 4
 6 e 8}
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
num
 cont: longint;
begin
   cont := 1; {pulou o 2}
   num := 1;
   repeat
      num := num + 2;
      if primo(num) then begin
         { write(num
 ' ');}
         cont := cont + 1;
      end;
   until cont = 10001;
   writeln;
   writeln('10001o. primo e'' '
 num)  { 104743 ?};
   readln;
end.
