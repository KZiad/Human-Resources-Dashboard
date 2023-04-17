class TrieNode {
    constructor() {
        this.children = {};
        this.endOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let curr = this.root;
        for (let c of word) {
            if (!(c in curr.children)) {
                curr.children[c] = new TrieNode();
            }
            curr = curr.children[c];
        }
        curr.endOfWord = true;
    }

    search(word) {
        let curr = this.root;
        for (let c of word) {
            if (!(c in curr.children)) {
                return false;
            }
            curr = curr.children[c];
        }
        return curr.endOfWord;
    }

    startsWith(prefix) {
        let curr = this.root;
        for (let c of prefix) {
            if (!(c in curr.children)) {
                return false;
            }
            curr = curr.children[c];
        }
        return true;
    }
}

function searchData() {

    const trie = new Trie();
    const employees = JSON.parse(localStorage.getItem("employees"));
    employees.forEach(employee => {
        console.log(employee.name);
        trie.insert(employee.name.toLowerCase());
    })

    document.addEventListener("DOMContentLoaded", () => {
        const table = document.querySelector('.search-div');
        const input = document.getElementById("search-input");
        let prev = table.innerHTML;

        input.addEventListener("input", () => {
            let result = '';

            const inputVal = input.value;
            const wordFound = trie.startsWith(inputVal);
            
            console.log(wordFound);
            if (wordFound) {
                employees.forEach(employee => {
                    if (employee.name.toLowerCase() === wordFound) {
                        const newRow = `
                            <tr>
                                <td><button type="button" class="emp-btn" onclick="window.location.href = 'employeeData.html'">${employee.name}</button></td>
                                <td>
                                    <button class="update-employee-btn" type="button" onclick="window.location.href='update.html';">Update</button>
                                    <button class="vacation-employee-btn" type="button" onclick="window.location.href='vacation.html';">Vacation</button>
                                </td>
                            </tr>
                        `;
                        prev = table.innerHTML;
                        table.innerHTML = newRow;
                    }
                });
                
            } else {
                table.innerHTML = "";
            }
        })

        input.addEventListener("keydown", (event) => {
            if (event.key == "Backspace") {
                table.innerHTML = prev;
            }
        })
    })
}
searchData();
