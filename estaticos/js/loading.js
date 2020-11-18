function loading(opcao) {
    if (opcao == 'login') {
        setTimeout(function () {
            window.location.href = "../principal";
        }, 2000);
    }
    else {
        setTimeout(function () {
            window.location.href = "../logout";
        }, 2000);
    }
}