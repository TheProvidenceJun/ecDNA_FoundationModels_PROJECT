<!--
last-updated: 2026-06-21
session-id: 2026-06-21-plan-fill
author-agent: cowork
-->

# roadmap.md — Phase A~E 전체

**한 줄**: Foundation model로 암세포 ecDNA를 single-cell 수준에서 characterize하고,
sequence와 cell state의 관계를 밝힌다.

**세 층위 질문**: cell-level(transcriptome만으로 carrier 구분?) / sequence-level(ecDNA
junction이 다른 amplification과 sequence에서 다른가?) / method-level(FM이 cancer-specific
구조를 학습했나?). 상세는 CLAUDE.md §2.

> **원칙**: 이 문서는 진실의 *지도*이지 사본이 아니다. 가이드를 복붙하지 않는다 —
> 진실이 두 곳으로 갈리면 rot다. 각 phase는 요약 + **"상세는
> `docs/knowledge/ecDNA_FM_guide.md` 참조"** 포인터로 둔다.
> 각 phase는 4칸: **목표 / 핵심작업 / 산출물 / 다음 phase로 가는 조건**.
> 마지막 칸이 핵심 — "끝나면 다음"이 아니라 **"결과가 ○○이면 이 길, ××이면 저 길"**
> (results-driven). 안 정해진 것을 정해진 척 적지 않는다.

---

## Phase A — Onboarding (배경·도구 학습 + dataset 확정)
> 상세: 가이드 "Phase A" (A.1~A.3).

- **목표**: 프로젝트에 필요한 배경 지식·도구를 익히고, 사용할 dataset list를 확정한다.
- **핵심작업**:
  - A.1 필수 reading — ecDNA biology(Wu 2019, Hung 2021, Lange 2022) + scFM(Geneformer, scGPT).
  - A.2 도구 학습 — scanpy(PBMC3K 전 과정), scFM API(Geneformer·scGPT embedding 추출), ground-truth pipeline(inferCNV/CopyKAT).
  - A.3 dataset 매핑 — AmpliconRepository 등록 → CCLE ecDNA line 추출 → scRNA-seq cross-reference(Kinker 2020, 개별 GEO) → target list 작성. **※ A.3은 codex가 아니라 사람(+도구1) 작업이다** (계정 인증 + 판단 섞인 큐레이션이라 자동화 대상 아님).
- **산출물**: dataset **target list** — 우선 cell line 3–5개 + 후보 5–10개.
- **다음 조건 (→ B)**: target list가 **확정**되어야 B 착수. dataset 매핑이 안 끝나면 B로 가지 않는다 (carrier detection은 데이터가 전제).

---

## Phase B — Frozen scFM × ecDNA carrier detection (메인 작업)
> 상세: 가이드 "Phase B" (B.1~B.5).

- **목표**: scFM이 **zero-shot**(별도 학습 없이)으로 ecDNA carrier cell을 transcriptome만 보고 구분할 수 있는지 평가한다. *frozen-first* (pretraining만으로 학습했나가 가장 흥미로운 질문 + compute·reproducibility 이점).
- **핵심작업**:
  - B.1 preprocessing — 3–5개 line scRNA-seq 통합, QC(Scrublet doublet, mito filter), normalization, batch effect 평가(kBET/LISI + UMAP).
  - B.2 unsupervised frozen embedding — Geneformer base / Geneformer cancer-tuned / scGPT 각각 zero-shot embedding → UMAP + Leiden. inferCNV로 carrier ground-truth label.
  - B.3 baseline 비교 — standard(HVG+PCA+Leiden), scVI.
  - B.4 linear probing — frozen embedding 위 logistic/MLP, carrier 분류. cell-line split(strict) + cell split 둘 다.
  - B.5 layer-wise probing — layer별 embedding의 probing 성능 (BERTology framework).
- **산출물**: clustering·probing 결과 + baseline 대비 정량지표(ARI, silhouette, carrier cluster purity).
- **다음 조건 (→ C, results-driven 분기)**:
  - frozen scFM이 carrier를 **잘 분리**하면 → C로 확장(cross cell-line + dosage)해서 일반성·정량 관계를 본다.
  - **약하지만 probing에 signal**이 있으면 → C에서 supervised/fine-tuning 비중을 키우는 쪽으로.
  - **거의 신호 없음**이면 → 왜 안 되는지(데이터·방법·전제)를 먼저 진단. C로 직진하지 않는다. (no도 결과다.)
  - 정확한 분기는 **Phase B 끝 미팅에서 사람과 결정**.

---

## Phase C — Cross cell-line + dosage 확장
> 가이드에 윤곽만 있음. 정직하게 얇게 둔다.

- **목표(한 줄)**: B에서 본 carrier detection을 더 많은 cell line과 ecDNA **dosage(copy 수)** 축으로 확장해 일반성과 정량 관계를 본다.
- **구체화 시점**: Phase B 결과를 보고 확정. (지금 더 적으면 추측이다.)

---

## Phase D — DNA FM × junction sequence 분석
> 가이드에 윤곽만 있음. 정직하게 얇게 둔다.

- **목표(한 줄)**: carrier cell이 carry하는 ecDNA의 **junction sequence**를 DNA FM으로 분석해 sequence-level signature가 있는지 본다 (sequence-level question).
- **구체화 시점**: 직전 phase 결과를 보고 확정.

---

## Phase E — (Optional) Structure layer
> 가이드에 윤곽만 있음. 정직하게 얇게 둔다.

- **목표(한 줄)**: (선택) Akita/Orca 등으로 3D structure layer를 얹어 multi-scale 이해를 보강한다.
- **구체화 시점**: D까지의 결과가 필요를 정당화할 때만. 기본은 optional.

---

> Phase C·D·E를 얇게 두는 것은 미완이 아니라 **설계**다. 각 phase의 결과가 다음을
> 정하므로, 안 정해진 것을 정해진 척 적는 것이 가장 나쁜 rot다.
