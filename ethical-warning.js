class EthicalWarning extends HTMLElement {
    connectedCallback() {
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                .warning-container {
                    background-color: #fff3cd;
                    border-left: 4px solid #ffc107;
                    padding: 1rem;
                    margin: 1rem 0;
                    border-radius: 0.25rem;
                    display: flex;
                    align-items: flex-start;
                }
                .warning-icon {
                    margin-right: 0.75rem;
                    color: #ffc107;
                    flex-shrink: 0;
                }
                .warning-content {
                    color: #856404;
                }
                .warning-title {
                    font-weight: 600;
                    margin-bottom: 0.5rem;
                }
            </style>
            <div class="warning-container">
                <div class="warning-icon">
                    <i data-feather="alert-triangle"></i>
                </div>
                <div class="warning-content">
                    <div class="warning-title">Ethical Use Required</div>
                    <div class="warning-text">
                        This tool should only be used on devices you own or have explicit permission to monitor.
                        Unauthorized use may violate privacy laws in your jurisdiction.
                    </div>
                </div>
            </div>
        `;
        
        //  feather icons DOM
        if (typeof feather !== 'undefined') {
            const icon = this.shadowRoot.querySelector('[data-feather]');
            feather.replace(icon);
        }
    }
}

customElements.define('ethical-warning', EthicalWarning);
