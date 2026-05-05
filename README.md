# IVR-For-Asterisk

ivr-project/<br>
├── README.md<br>
├── extensions/<br>
│   ├── ivr-menugeral.conf<br>
│   ├── ivr-varejista.conf<br>
│   ├── ivr-fornecedor.conf<br>
│   ├── ivr-colaborador.conf<br>
│   ├── ivr-consumidor.conf<br>
│   ├── ivr-trabalheconosco.conf<br>
├── agi/<br>
│   └── (placeholders)<br>


# IVR Project (Asterisk)

This project implements a multi-layer IVR system using Asterisk.

## Structure

- Main entry point: `ivr-menugeral`
- Segmented flows:
  - Retail (varejista)
  - Consumer (consumidor)
  - Supplier (fornecedor)
  - Employee (colaborador)
  - Careers (trabalheconosco)

## Features

- Modular IVR contexts
- Input validation with retry logic (CPF/CNPJ)
- Call routing based on user profile
- Queue fallback for human assistance
- Placeholder hooks for AGI integration

## Notes

- AGI calls are placeholders and must be implemented
- Audio files should be placed under `/var/lib/asterisk/sounds/custom`
