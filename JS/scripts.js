const resultadosExercicios = document.querySelector('[resultados-exercicios]')

var body = document.querySelector('body')

function res1000() {
    resposta = 'Hello world!'
    return resposta
    
}

function res1001() {
    let a = 10
    let b = 9
    let x = a + b
    return x
}

function res1002() {
    let n = 3.14159
    let r = 2
    let a = n * Math.pow(r, 2)
    return a.toFixed(4)
}

function res1003() {
    let a = 30
    let b = 10
    let soma = a + b
    return soma
}

function res1004() {
    let a = 3
    let b = 9
    let prod = a * b
    return prod
}

function res1005() {
    let a = 5 * 3.5
    let b = 7.1 * 7.5 
    let avg1 = (a + b) / (7.5 + 3.5)
    return avg1.toFixed(5)
}

function res1006() {
    let a = 5 * 2
    let b = 6 * 3
    let c = 7 * 5
    let avg2 = (a + b + c)/ (2 + 3 + 5)
    return avg2.toFixed(1)
}

function res1007() {
    let a = 5
    let b = 6
    let c = 7
    let d = 8
    let diff = a * b - c * d
    return diff
}

class Res1008 {
    constructor(codigoColaborador, valorHora, horasTrabalhadas, salarioDevido) {
        this.codigoColaborador = codigoColaborador
        this.valorHora = valorHora
        this.horasTrabalhadas = horasTrabalhadas
        this.salarioDevido = valorHora * horasTrabalhadas
    }
}

function res1008() {
    let colaborador = new Res1008(25, 5.5, 100)
    return colaborador
}

function res1009() {
    let nomeColaborador = 'JOAO'
    let salarioFixo = 500
    totalVendas = 1230.30
    let salarioTotal = salarioFixo + totalVendas * 0.15
    return salarioTotal
}

function res1010() {
    let codProd1 = 12
    let unidProd1 = 1
    let precoUnitProd1 = 5.3

    let codProd2 = 16
    let unidProd2 = 2
    let precoUnitProd2 = 5.1

    let valorPagar = (unidProd1 * precoUnitProd1) + (unidProd2 * precoUnitProd2)
    
    return valorPagar
}

function res1011() {
    r = 3
    v = (4.0 / 3.0) * 3.14159 * Math.pow(r, 3)

    return v
}

console.log("Resultado ex 1000: " + res1000()) 
console.log("Resultado ex 1001: X = " + res1001()) 
console.log("Resultado ex 1002: A = " + res1002()) 
console.log("Resultado ex 1003: SOMA = " + res1003()) 
console.log("Resultado ex 1004: PROD = " + res1004())
console.log("Resultado ex 1005: MEDIA = " + res1005())
console.log("Resultado ex 1006: MEDIA = " + res1006())
console.log("Resultado ex 1007: DIFERENCA = " + res1007())
console.log("Resultado ex 1008: " + '\n' + "NUMBER = " + res1008().codigoColaborador + '\n' + 
"SALARY = U$ " + res1008().salarioDevido.toFixed(2))
console.log("Resultado ex 1009: TOTAL = " + res1009().toFixed(2))
console.log("Resultado ex 1010: VALOR A PAGAR: R$ " + res1010().toFixed(2))
console.log("Resultado ex 1011: VOLUME = " + res1011().toFixed(3))



