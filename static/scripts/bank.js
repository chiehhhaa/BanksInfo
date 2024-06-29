function bankData() {
    return {
        search: '',
        searchPlaceholder: '請輸入關鍵字或銀行代碼...',
        showDropdown: false,
        selectedBank: null,
        branchSearch: '',
        branchSearchPlaceholder: '請選擇分行名稱...',
        showBranchDropdown: false,
        selectedBranch: null,
        banks: [],
        filteredBanks: [],
        branches: [],
        filteredBranches: [],
        branchDetail: {},
        baseUrl: window.location.origin,

        async init() {
            const response = await fetch('/api/banks/');
            this.banks = await response.json();
            this.filteredBanks = this.banks;
        },

        filterBanks() {
            const keyword = this.search.toLowerCase();
            this.filteredBanks = this.banks.filter(bank => {
                return bank.name.toLowerCase().includes(keyword) || bank.bank_code.includes(keyword);
            });
        },

        async updateBranches() {
            if (!this.selectedBank) {
                this.branches = [];
                this.filteredBranches = [];
                return;
            }
            const response = await fetch(`/api/banks/${this.selectedBank}/branches/`);
            this.branches = await response.json();
            this.filteredBranches = this.branches;
        },

        filterBranches() {
            const keyword = this.branchSearch.toLowerCase();
            this.filteredBranches = this.branches.filter(branch => {
                return branch.name.toLowerCase().includes(keyword);
            });
        },

        async selectBank(bank) {
            this.searchPlaceholder = `${bank.bank_code} ${bank.name}`;
            this.search = '';
            this.selectedBank = bank.id;
            this.branchSearch = '';
            this.selectedBranch = null;
            this.updateBranches();
            this.showDropdown = false;
            this.search = `${bank.bank_code} ${bank.name}`;
            history.pushState(null, '', `/${bank.bank_code}/`);
            this.removeDetail();
        },

        async selectBranch(branch) {
            this.branchSearchPlaceholder = branch.name;
            this.branchSearch = '';
            this.selectedBranch = branch.id;
            const response = await fetch(`/api/branches/${branch.id}`);
            this.branchDetail = await response.json();
            this.showBranchDropdown = false;
            const bank = this.banks.find(b => b.id === this.selectedBank);
            if (bank) {
                const url = `${this.baseUrl}/${bank.bank_code}/${branch.branch_code}/${bank.name}-${branch.name}.html`;
                history.pushState(null, '', url);
            }
            this.removeDetail();
        },

        removeDetail() {
            const detailContainer = document.querySelector('.detail-container');
            if (detailContainer) {
                detailContainer.innerHTML = '';
            }
        },

        hideDropdown() {
            setTimeout(() => {
                this.showDropdown = false;
            }, 200);
        },

        hideBranchDropdown() {
            setTimeout(() => {
                this.showBranchDropdown = false;
            }, 200);
        },

        clearAndShowDropdown() {
            this.search = '';
            this.showDropdown = true;
        },

        clearAndShowBranchDropdown() {
            this.branchSearch = '';
            this.showBranchDropdown = true;
        },

        selectedBankNameWithCodeAndBranch() {
            if (this.selectedBank && this.selectedBranch) {
                const bank = this.banks.find(b => b.id === this.selectedBank);
                const branch = this.branches.find(b => b.id === this.selectedBranch);
                if (bank && branch) {
                    return `${bank.name} (${bank.bank_code}) ${branch.name}`;
                }
            }
            return '';
        },

        copyBranchCode(branchCode, event) {
            const button = event.target;
            button.textContent = '已複製';
            navigator.clipboard.writeText(branchCode)
                .then(() => {
                    setTimeout(() => {
                        button.textContent = '複製分行代碼';
                    }, 500);
                })
                .catch(err => {
                    console.error('複製分行代碼失敗: ', err);
                });
        },

        copyBranchUrl() {
            const url = this.generateBranchUrl();
            if (url) {
                navigator.clipboard.writeText(url)
                    .then(() => {
                        const button = document.querySelector('.copy-url-button');
                        if (button) {
                            button.textContent = '已複製';
                            setTimeout(() => {
                                button.textContent = '複製分行網址';
                            },  500);
                        }
                    })
                    .catch(err => {
                        console.error('複製分行網址失敗: ', err);
                    });
            }
        },

        resetSelections() {
            this.selectedBank = null;
            this.selectedBranch = null;
            this.branchDetail = {};
            this.search = '';
            this.branchSearch = '';
            this.searchPlaceholder = '請輸入關鍵字或銀行代碼...';
            this.branchSearchPlaceholder = '請選擇分行名稱...';
        },

        generateBranchUrl() {
            const bank = this.banks.find(b => b.id === this.selectedBank);
            const branch = this.branches.find(b => b.id === this.selectedBranch);
            if (bank && branch) {
                return `${this.baseUrl}/${bank.bank_code}/${branch.branch_code}/${bank.name}-${branch.name}.html`;
            }
            return null; 
        }
    };
}