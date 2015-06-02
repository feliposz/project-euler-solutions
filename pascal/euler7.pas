program euler7;

var
  primes : array [1..10001] of longint;
  nprimes, i : integer;
  num : longint;
  isprime : boolean;
  
begin
  primes[1] := 2;
  nprimes := 1;
  num := 3;
  while (nprimes < 10001) do
  begin
    isprime := true;
    for i := 1 to nprimes do
    begin
      if (num mod primes[i] = 0) then
      begin
        isprime := false;
        break;
      end;
    end;
    if isprime then
    begin
      inc(nprimes);
      primes[nprimes] := num;
    end;
    num := num + 2;
  end;
  writeln(primes[10001]);  
end.