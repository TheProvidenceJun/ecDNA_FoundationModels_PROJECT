<!--
last-updated: 2026-06-22
session-id: 2026-06-22-constraints
author-agent: cowork
-->

# constraints.md — 금지가 실제로 어떻게 강제되나 (집행 장부)

> `roles.md`가 **권한 지도**("누가 무엇을 못 하나")라면, 이 문서는 **집행 장부**
> ("그 금지가 실제로 어떻게 강제되나")다. 규칙을 다시 나열하지 않는다 — 각 규칙 옆에
> **집행 수단**과 **현재 강제 상태**를 단다. (규칙 자체의 정의는 roles.md / CLAUDE.md §4 /
> AGENTS.md §3 참조.)
>
> **가장 중요한 원칙 — soft를 hard인 척 쓰지 마라.** 능력(can't)과 약속(shouldn't)을
> 구별한다. 메커니즘이 실제로 켜져 있지 않은데 "강제됨"이라 적으면, 그게 가장 위험한
> rot다(모두가 안전하다고 착각). 아래 상태값은 **사람이 환경을 실제 점검한 결과**이며,
> 추측으로 바꾸지 않는다.

---

## 상태 용어 정의 (먼저 읽을 것)

| 용어 | 뜻 |
|---|---|
| **적용됨** | 메커니즘이 실제로 작동 중. (hard) |
| **가능하나 미설정** | 메커니즘을 켤 수 있으나 아직 안 켬. (전환 가능한 soft) |
| **soft** | 강제 메커니즘이 **없음을 확인**함. 자기규율·사후검증에만 의존. |
| **미확인** | 아직 점검 못 함. **"없다고 확인한 게 아니다" — soft와 다르다.** |

> 특히 **미확인 ≠ soft**. soft는 "메커니즘 없음을 확인", 미확인은 "있는지 없는지 아직 모름".
> 이 둘을 섞으면 거짓 안심 또는 거짓 불안이 된다.

---

## 강제 메커니즘 표 (2026-06-22 환경 점검 기준)

| 규칙 (무엇을 금지)                                          | 강제 메커니즘 (어디서)            | 현재 상태                                                          |
| ---------------------------------------------------- | ------------------------ | -------------------------------------------------------------- |
| git commit/push 사람 전용                                | pre-commit hook          | **soft** — hook 없음 확인됨(`.git/hooks/`에 `pre-commit.sample`만 존재) |
| codex가 main에 직접 push 금지                              | GitHub branch protection | **가능하나 미설정** — 원격 존재(`origin`), 보호 규칙 미구성 확인됨                  |
| `data/` git 비추적                                      | `.gitignore`             | **적용됨** — `.gitignore`에 `data/` 항목 확인됨                         |
| codex의 constitution/plan/state/specs/decisions 수정 금지 | read-only 마운트 / sandbox  | **미확인** — smoke test에서 점검                                      |
| codex sandbox 경계(지정 폴더 외 접근 금지)                      | codex-GUI 설정             | **미확인** — codex 실제 구동 시 점검                                     |
| cowork의 코드/데이터 직접수정 금지                               | (없음)                     | **soft** — 자기규율                                                |
| codex의 report 의무(report 없는 변경 무효)                    | cowork 사후검증              | **soft** — 검증 단계에서만                                            |
| 위험작업(영구삭제·권한변경·외부공유) 사람 승인 없이 금지                     | (없음)                     | **soft** — 자기규율                                                |

> 요약: **적용됨 1개**(.gitignore data/), **가능하나 미설정 1개**(branch protection),
> **미확인 2개**(codex 마운트·sandbox), **soft 4개**(자기규율·사후검증). 대부분의 경계는
> 아직 환경이 아니라 규율이 지키고 있다.

---

## hard 전환 로드맵

**지금은 hard 전환을 하지 않는다.** 이유: codex를 아직 한 번도 안 돌려봤다. codex의
실제 행동(경계를 존중하나/무시하나)을 **smoke test에서 본 뒤**, 실제로 뚫리는 규칙부터
hard로 막는다. (성급한 hard화는 켜는 비용만 들고 정작 안 뚫리는 곳을 막는 낭비일 수 있다.)

### hard 후보 우선순위 (사람 합의)
1. **1순위 — codex의 constitution/plan/state 수정 금지.** 뚫리면 메모리·제약이 통째로 붕괴.
2. **2순위 — git commit/push 사람 전용.** branch protection으로 hard화 가능(환경 확인됨).
3. **3순위 — report 의무.** cowork 사후검증으로 일부는 이미 잡힘.

### hard화 수단 후보 (참고 메뉴 — '할 수 있다'이지 '했다'가 아님)
> 아래는 어느 수단이 어느 규칙에 쓰일 수 있는지의 1:1 매핑이다. **실제 적용 전까지
> 위 표의 상태는 바뀌지 않는다.**

| 수단 | 쓰일 수 있는 규칙 | 현재 |
|---|---|---|
| read-only 마운트 | codex의 docs 수정 금지 (1순위) | 미적용 (미확인) |
| GitHub branch protection + PR 게이트 | codex의 main push 금지 (2순위) | 미적용 (가능하나 미설정) |
| codex sandbox approval mode | codex 폴더 경계 / 위험작업 승인 | 미적용 (미확인) |
| pre-commit hook | commit 게이트(형식·금지) | 미적용 (soft) |
| `.gitignore` | `data/` 비추적 | **적용됨** |

---

## 열린 항목 (smoke test 또는 그 전후에 다룸)

- GitHub branch protection 실제 설정 여부 → 설정하면 "적용됨"으로 갱신.
- codex sandbox / read-only 마운트 점검 → smoke test에서 codex 실제 행동으로 확인.
- pre-commit hook 도입 여부 → 커밋 게이트가 필요하다고 판단되면.

> 이 표는 `AGENTS.md §7` 강제상태 표와 **일관**되어야 한다. 이번 점검으로 일부 상태가
> 갱신되어 AGENTS.md §7과 불일치가 생겼을 수 있다(예: AGENTS §7은 "전부 soft"). 그
> 불일치 목록은 이번 세션에 cowork가 사람에게 보고하며, **AGENTS.md 수정은 별도로** 한다.
