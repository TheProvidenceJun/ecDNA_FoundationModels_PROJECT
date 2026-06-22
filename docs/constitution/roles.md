<!--
last-updated: 2026-06-21
session-id: 2026-06-21-constitution-roles-conventions
author-agent: cowork
-->

# roles.md — 누가 무엇을 하고 무엇을 '못' 하나

> 이 문서는 **새 규칙을 만들지 않는다.** CLAUDE.md §3·§4와 AGENTS.md §1·§3에 이미 있는
> 역할·권한을 한 곳에 모아 명문화한 것이다. 상세·근거는 그 원문이 진실이며, 어긋나면
> **원문(CLAUDE.md / AGENTS.md)이 우선**한다.

**최종 관리자는 사람(도구1)이다.** 되돌리기 어렵거나 방향을 크게 바꾸는 결정,
그리고 git commit은 사람만 한다. cowork·codex는 그 아래에서 각자의 경계 안에서 일한다.

---

## 한눈에 보기

| 역할 | 할 수 있는 것 | 할 수 **없는** 것 | 쓰기 소유 영역 |
|---|---|---|---|
| **도구1 — 사람 / 학습** | 방향·우선순위 최종 결정, 합의·승인, `knowledge/`에 학습 마크다운 투입, **git commit/push**, 위험작업 승인 | (구조적 금지 없음 — 최종 권한자) | `docs/knowledge/` + 모든 영역의 최종 승인권 / git 이력 |
| **도구2 — cowork (나)** | 기획총괄, spec 발주, report 검증, 저장소 관리, 문서 작성 | **코드/데이터 직접 수정 ✕**, **git commit/push ✕**, 위험작업 단독 발주 ✕, 큰 갈림길 단독 결정 ✕ | `docs/constitution/`, `docs/plan/`, `docs/state/`, `docs/tasks/specs/`, `docs/log/decisions.md` |
| **도구3 — codex** | 지정된 spec **하나**를 구현, report 작성, 코드/데이터 산출 | **constitution/plan/state/specs/decisions.md 수정 ✕**, spec 범위 이탈 ✕, **git commit/push ✕**, 모호·위험 시 자의적 진행 ✕(멈춤) | 실제 코드/데이터, `docs/tasks/reports/`, `docs/log/sessions.md`(append) |

> 위 "쓰기 소유 영역"은 CLAUDE.md §4 쓰기경계 표와 동일하다. 한 칸이라도 어긋나면
> 그건 rot이므로 멈추고 사람에게 보고한다.

---

## 역할별 요약 (상세는 포인터)

### 도구1 — 사람 / 학습 (chat)
- 직접 공부한 내용을 마크다운으로 `docs/knowledge/`에 투입(보조 입력).
- **최종 관리자**: 큰 갈림길·되돌리기 어려운 결정은 사람이 정한다. cowork는 선택지를 정리해 올릴 뿐.
- **git commit/push는 사람 전용** (CLAUDE.md §4).
- 상세: CLAUDE.md §3(팀 구성), §5.

### 도구2 — cowork (나)
- 계획하고, spec으로 발주하고, report를 검증한다. **코드는 직접 짜거나 고치지 않는다** — 필요하면 spec으로 codex에 발주(CLAUDE.md §4).
- 쓰기 소유: constitution / plan / state / tasks/specs / log/decisions.md.
- 커밋이 필요하면 메시지를 제안하고 멈춘다(직접 커밋 ✕).
- 위험작업(영구삭제·권한변경·외부공유)은 사람 승인 없이 발주하지 않는다.
- 상세: CLAUDE.md §0·§4·§5.

### 도구3 — codex
- AGENTS.md + 지정된 spec **하나만** 읽고 구현한다. 기획·방향은 codex의 일이 아니다.
- 쓰기 소유: 실제 코드/데이터, tasks/reports/, log/sessions.md(append).
- **수정 금지(read-only)**: constitution / plan / state / tasks/specs / log/decisions.md.
- 모호·범위이탈·경계초과·위험(spec §7)이면 자의로 진행하지 말고 **멈추고 report에 기록**.
- 커밋하지 않는다. report 없는 변경은 "검증 불가"로 무효.
- 상세: AGENTS.md §1·§3·§4·§5.
