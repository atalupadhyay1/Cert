# Authoritative Sources & Skill Coverage (`MCP`)

All `600` questions and `120` canonical option/sequence rationales in `course/MCP/` are authored originally from public specifications, standards, and engineering documentation verified as of **November 2026**. Zero recalled exam items or proprietary vendor sample-company names are used.

## 1. Primary Certification & Standards Baselines

1. **Model Context Protocol Specification (`2025-11-25`, plus `2025-06-18` / `2025-03-26`):** Tools, Resources, Prompts, `stdio` vs `Streamable HTTP` (`Mcp-Session-Id`/`Last-Event-ID`), sampling, roots, elicitation — <https://modelcontextprotocol.io/specification/2025-11-25> & <https://github.com/modelcontextprotocol/specification>
2. **MCP Registry & Inspector:** Signed server distribution, `server.json` schema, `npx @modelcontextprotocol/inspector` UI + CLI — <https://github.com/modelcontextprotocol/registry> & <https://github.com/modelcontextprotocol/inspector>
3. **MCP SDKs:** TypeScript `@modelcontextprotocol/sdk` (`McpServer` + Zod) and Python `mcp` (`FastMCP` + Pydantic) — <https://github.com/modelcontextprotocol/typescript-sdk> & <https://github.com/modelcontextprotocol/python-sdk>
4. **OAuth 2.1 & IETF RFCs:** `RFC 7591` DCR, `RFC 8707` Resource Indicators, `RFC 9207` `iss` validation, `RFC 9728` Protected Resource Metadata, `CIMD` — <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12> & <https://datatracker.ietf.org/doc/html/rfc9207>
5. **Linux Foundation Agentic AI Foundation (`AAIF`):** Open governance for `MCP`, `A2A`, `AGENTS.md` — <https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation>
6. **OWASP MCP Security Checklist & GenAI Security:** Tool poisoning, rug-pull, privilege escalation, prompt injection mitigations — <https://genai.owasp.org/resource/mcp-security-checklist/>
7. **Agent2Agent (`A2A`) & Gateway Mesh:** Horizontal peer delegation vs vertical MCP tool attachment — <https://a2a-protocol.org/latest/>

## 2. Coverage Matrix Across All `34` Skills (`600` Questions)

Every exam set (`Set 1` through `Set 6`) enforces the exact `SKILL_PLAN` in `04-resources/bank.py`:
- **Domain 1 (`18`/set · `108` total):** `1.1` (`3`), `1.2` (`3`), `1.3` (`3`), `1.4` (`3`), `1.5` (`3`), `1.6` (`3`)
- **Domain 2 (`20`/set · `120` total):** `2.1` (`4`), `2.2` (`4`), `2.3` (`3`), `2.4` (`3`), `2.5` (`3`), `2.6` (`3`)
- **Domain 3 (`16`/set · `96` total):** `3.1` (`3`), `3.2` (`3`), `3.3` (`3`), `3.4` (`3`), `3.5` (`2`), `3.6` (`2`)
- **Domain 4 (`16`/set · `96` total):** `4.1` (`3`), `4.2` (`3`), `4.3` (`3`), `4.4` (`3`), `4.5` (`2`), `4.6` (`2`)
- **Domain 5 (`15`/set · `90` total):** `5.1` (`3`), `5.2` (`3`), `5.3` (`3`), `5.4` (`3`), `5.5` (`3`)
- **Domain 6 (`15`/set · `90` total):** `6.1` (`3`), `6.2` (`3`), `6.3` (`3`), `6.4` (`3`), `6.5` (`3`)

