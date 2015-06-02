program euler11;

const
  ROWS = 20;
  COLS = 20;

type
   TDirection = ( HORIZONTAL, VERTICAL, DIAGONAL1, DIAGONAL2 );

var
  data: array[1..ROWS, 1..COLS] of integer;
  max_prod: longint;

procedure load_data;
var
  str: string;
  i, j, error: integer;
  filedata: text;
begin
  assign(filedata, 'c:\dev\projects\project euler\euler11.dat');
  reset(filedata);
  for i := 1 to ROWS do
  begin
    readln(filedata, str);
    for j := 1 to COLS do
    begin
      val(copy(str, (j-1)*3+1, 2), data[i, j], error);
    end;
  end;
  close(filedata);
end;

procedure print_data;
var
  i, j: integer;
begin
  for i := 1 to ROWS do
  begin
    for j := 1 to COLS do
    begin
      write(data[i,j]:2, ' ');
    end;
    writeln;
  end;
end;

procedure update_max_prod(prod: longint);
begin
  if (prod > max_prod) then
    max_prod := prod;
end;

procedure check_line(direction: TDirection);
var
  i, j, k: integer;
  prod: longint;
  min_rows, min_cols, max_rows, max_cols, drow, dcol: integer;
begin
   
  drow := 0; min_rows := 1; max_rows := ROWS - 3;
  dcol := 0; min_cols := 1; max_cols := COLS - 3;

  case direction of
    HORIZONTAL: begin dcol := 1; max_rows := ROWS; end;
    VERTICAL:   begin drow := 1; max_cols := COLS; end;
    DIAGONAL1:  begin drow := 1; dcol :=  1; end;
    DIAGONAL2:  begin drow := 1; dcol := -1; min_cols := 4; end;
  end;

  for i := min_rows to max_rows do
  begin
    for j := min_cols to max_cols do
    begin
      prod := 1;
      for k := 0 to 3 do
        prod := prod * data[i + (k*drow), j + (k*dcol)];
      update_max_prod(prod);
    end;
  end;

end;

begin
  load_data;
  {print_data;} {just to check if data loaded correctly}
  check_line(HORIZONTAL);
  check_line(VERTICAL);
  check_line(DIAGONAL1);
  check_line(DIAGONAL2);
  writeln(max_prod);
  readln;
end.
