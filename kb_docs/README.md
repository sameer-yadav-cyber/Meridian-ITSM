# Knowledge Base files

`Meridian_KB.md` is the approved Phase 1 article set (Hardware, Network, Applications, Access Management, Service Catalogue).

## Load into AEX

1. Open `Meridian_KB.md`.
2. Export or print to PDF (Word, VS Code Markdown PDF, or similar). Keep article headings (`## KB-xx-###`) intact so indexing chunks by article.
3. Upload the PDF to the AEX Knowledge Base collection used by this agent.
4. Run index/reindex in AEX.
5. The agent SOP (`../meridian.txt`) retrieves **at most three** ranked articles from that collection. It does not use MeridianDesk `/kb/search` for full text.

Articles are written so retrieval can match symptoms, error language, and domain names.
