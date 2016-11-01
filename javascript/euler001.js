/*
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer:
233168
*/

// Solução 1:

function euler1(max) {
    var resultado = 0;
    for (var i = 1; i < max; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            resultado += i;
        }
    }
    return resultado;
}

// Solução 2:

// fórmula da PA considerando primeiro, último e qtde
function progressao_aritmetica(primeiro, ultimo, qtde) {
    return (primeiro + ultimo) * qtde / 2;
}

// Maior múltiplo de um número que seja <= máximo
function multiplo_menor_que(multiplicador, maximo) {
    return Math.floor(maximo / multiplicador) * multiplicador;
}

function euler1b(max) {
    var max_mult3 = multiplo_menor_que(3, max-1);
    var max_mult5 = multiplo_menor_que(5, max-1);
    var max_mult15 = multiplo_menor_que(15, max-1);

    // Todos os múltiplos de 3 + todos os múltiplos de 5 - todos os múltiplos de 15 (3 * 5)
    return progressao_aritmetica(3, max_mult3, max_mult3 / 3) 
         + progressao_aritmetica(5, max_mult5, max_mult5 / 5) 
         - progressao_aritmetica(15, max_mult15, max_mult15 / 15);
}

// Solução 3:

function termo_pa(primeiro, fator, n) {
    return primeiro + (n - 1) * fator;
}

// fórmula da PA considerando primeiro, fator e qtde
function progressao_aritmetica2(primeiro, fator, qtde) {
    var ultimo = termo_pa(primeiro, fator, qtde);
    return (primeiro + ultimo) * qtde / 2;
}

// qtde multiplos que existem até um número
function multiplos_ate(multiplicador, maximo) {
    return Math.floor(maximo / multiplicador);
}

function euler1c(max) {
    var qtde_mult3 = multiplos_ate(3, max-1);
    var qtde_mult5 = multiplos_ate(5, max-1);
    var qtde_mult15 = multiplos_ate(15, max-1);

    // Todos os múltiplos de 3 + todos os múltiplos de 5 - todos os múltiplos de 15 (3 * 5)
    return progressao_aritmetica2(3, 3, qtde_mult3) 
         + progressao_aritmetica2(5, 5, qtde_mult5) 
         - progressao_aritmetica2(15, 15, qtde_mult15);
}

// Solução 4:

function multiplos_ate(multiplicador, maximo) {
    return Math.floor(maximo / multiplicador);
}

// Lembrando que:
// 1 + 2 + 3 + 4 + ... + p = (1 + p) * p / 2 [ simplificação da fórmula da PA => (primeiro + ultimo) * qtde / 2 ]

function soma_multiplos_ate(divisor, maximo) {
    qtde_multiplos = multiplos_ate(divisor, maximo);
    return divisor * qtde_multiplos;
}

function euler1d(max) {
    // Todos os múltiplos de 3 + todos os múltiplos de 5 - todos os múltiplos de 15 (3 * 5)
    return soma_multiplos_ate(3, max-1) + soma_multiplos_ate(5, max-1) - (15, max-1);
}
