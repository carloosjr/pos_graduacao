function formatarCEP(input) {
    let cep = input.value.replace(/\D/g, '');
    let formattedCEP = cep.slice(0, 5) + cep.slice(5);
    input.value = formattedCEP;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('cepInput').addEventListener('input', function() {
        let cep = this.value.replace(/\D/g, '');

        if (cep.length === 8) {
            buscarCEP();
        }
    });
});

function buscarCEP() {
    let cep = document.getElementById('cepInput').value.replace(/\D/g, '');

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
            if (!data.erro) {
                document.getElementById('logradouroInput').value = data.logradouro;
                document.getElementById('bairroInput').value = data.bairro;
                document.getElementById('cidadeInput').value = data.localidade;
                document.getElementById('estadoInput').value = data.uf;
                //hideErrorMessage(); // Esconde a mensagem de erro, caso esteja sendo exibida
            } else {
                resetFields();
                displayErrorMessage("CEP não localizado.");
            }
        })
        .catch(() => {
            resetFields();
            displayErrorMessage("Ocorreu um erro ao buscar o CEP. Por favor, tente novamente.");
        });
}

function displayErrorMessage(message) {
    let errorMessageElement = document.getElementById('cepErrorMessage');
    if (!errorMessageElement) {
        errorMessageElement = document.createElement('span');
        errorMessageElement.id = 'cepErrorMessage';
        errorMessageElement.style.color = 'red';
        errorMessageElement.textContent = message;
        document.getElementById('cepInput').parentNode.appendChild(errorMessageElement);
    } else {
        errorMessageElement.textContent = message;
    }
}

function hideErrorMessage() {
    let errorMessageElement = document.getElementById('cepErrorMessage');
    if (errorMessageElement) {
        errorMessageElement.remove();
    }
}
