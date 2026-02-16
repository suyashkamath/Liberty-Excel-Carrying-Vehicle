# # # # # # from fastapi import FastAPI, File, UploadFile, HTTPException
# # # # # # from fastapi.middleware.cors import CORSMiddleware
# # # # # # from fastapi.responses import FileResponse, JSONResponse
# # # # # # import pandas as pd
# # # # # # import io
# # # # # # import os
# # # # # # from typing import List, Dict, Tuple, Optional
# # # # # # from datetime import datetime
# # # # # # import traceback
# # # # # # import tempfile

# # # # # # app = FastAPI(title="Carrying Vehicles Payout Processor API")

# # # # # # app.add_middleware(
# # # # # #     CORSMiddleware,
# # # # # #     allow_origins=["*"],  
# # # # # #     allow_credentials=True,
# # # # # #     allow_methods=["*"],
# # # # # #     allow_headers=["*"],
# # # # # # )

# # # # # # FORMULA_DATA = [
# # # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
# # # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
# # # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
# # # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# # # # # # ]

# # # # # from fastapi import FastAPI, File, UploadFile, HTTPException
# # # # # from fastapi.middleware.cors import CORSMiddleware
# # # # # from fastapi.responses import FileResponse, JSONResponse
# # # # # import pandas as pd
# # # # # import io
# # # # # import os
# # # # # from typing import List, Dict, Tuple, Optional
# # # # # from datetime import datetime
# # # # # import traceback
# # # # # import tempfile

# # # # # app = FastAPI(title="Carrying Vehicles Payout Processor API")

# # # # # app.add_middleware(
# # # # #     CORSMiddleware,
# # # # #     allow_origins=["*"],  
# # # # #     allow_credentials=True,
# # # # #     allow_methods=["*"],
# # # # #     allow_headers=["*"],
# # # # # )

# # # # # # ===============================================================================
# # # # # # FORMULA DATA
# # # # # # ===============================================================================
# # # # # FORMULA_DATA = [
# # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
# # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
# # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
# # # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# # # # # ]

# # # # # # ===============================================================================
# # # # # # STATE MAPPING
# # # # # # ===============================================================================
# # # # # STATE_MAPPING = {
# # # # #     "ANDHRA PRADESH": "ANDHRA PRADESH",
# # # # #     "KRISHNA": "ANDHRA PRADESH",
# # # # #     "VIJAYWADA": "ANDHRA PRADESH",
# # # # #     "VIJAYAWADA": "ANDHRA PRADESH",
# # # # #     "VISAKHAPATNAM": "ANDHRA PRADESH",
    
# # # # #     "KARNATAKA": "KARNATAKA",
# # # # #     "BANGALORE": "KARNATAKA",
# # # # #     "BENGALURU": "KARNATAKA",
    
# # # # #     "KERALA": "KERALA",
# # # # #     "ERNAKULAM": "KERALA",
# # # # #     "COCHIN": "KERALA",
    
# # # # #     "TAMIL NADU": "TAMIL NADU",
# # # # #     "CHENNAI": "TAMIL NADU",
# # # # #     "PONDICHERRY": "TAMIL NADU",
    
# # # # #     "TELANGANA": "TELANGANA",
# # # # #     "HYDERABAD": "TELANGANA",
    
# # # # #     "MAHARASHTRA": "MAHARASHTRA",
# # # # #     "MUMBAI": "MAHARASHTRA",
# # # # #     "PUNE": "MAHARASHTRA",
# # # # #     "NAGPUR": "MAHARASHTRA",
    
# # # # #     "MADHYA PRADESH": "MADHYA PRADESH",
# # # # #     "BHOPAL": "MADHYA PRADESH",
# # # # #     "GWALIOR": "MADHYA PRADESH",
# # # # #     "JABALPUR": "MADHYA PRADESH",
    
# # # # #     "CHANDIGARH": "CHANDIGARH",
# # # # #     "DELHI": "DELHI",
# # # # #     "NCR": "DELHI",
# # # # #     "GOA": "GOA",
    
# # # # #     "HIMACHAL PRADESH": "HIMACHAL PRADESH",
# # # # #     "BILASPUR": "HIMACHAL PRADESH",
# # # # #     "MANDI": "HIMACHAL PRADESH",
# # # # #     "SOLAN": "HIMACHAL PRADESH",
# # # # #     "SHIMLA": "HIMACHAL PRADESH",
# # # # #     "MANALI": "HIMACHAL PRADESH",
# # # # # }

# # # # # uploaded_files = {}

# # # # # # ===============================================================================
# # # # # # HELPER FUNCTIONS
# # # # # # ===============================================================================

# # # # # def cell_to_str(val) -> str:
# # # # #     """Safely convert ANY cell value to string."""
# # # # #     if val is None:
# # # # #         return ""
# # # # #     try:
# # # # #         if pd.isna(val):
# # # # #             return ""
# # # # #     except (TypeError, ValueError):
# # # # #         pass
# # # # #     return str(val).strip()


# # # # # def safe_float(value) -> Optional[float]:
# # # # #     """Safely convert value to float, handling percentages."""
# # # # #     if value is None:
# # # # #         return None
# # # # #     try:
# # # # #         if pd.isna(value):
# # # # #             return None
# # # # #     except (TypeError, ValueError):
# # # # #         pass
    
# # # # #     s = str(value).strip().upper().replace("%", "")
# # # # #     if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
# # # # #         return None
    
# # # # #     try:
# # # # #         num = float(s)
# # # # #         if num < 0:
# # # # #             return None
# # # # #         return num * 100 if 0 < num < 1 else num
# # # # #     except Exception:
# # # # #         return None


# # # # # def map_state(location: str) -> str:
# # # # #     """Map location to state."""
# # # # #     location_upper = location.upper()
    
# # # # #     for key, val in STATE_MAPPING.items():
# # # # #         if key.upper() in location_upper:
# # # # #             return val
    
# # # # #     return location


# # # # # def get_payin_category(payin: float) -> str:
# # # # #     """Get payin category."""
# # # # #     if payin <= 20:
# # # # #         return "Payin Below 20%"
# # # # #     elif payin <= 30:
# # # # #         return "Payin 21% to 30%"
# # # # #     elif payin <= 50:
# # # # #         return "Payin 31% to 50%"
# # # # #     else:
# # # # #         return "Payin Above 50%"


# # # # # def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
# # # # #     """
# # # # #     Calculate payout for CV based on payin ranges.
# # # # #     CV is independent of policy type - uses tiered deductions.
# # # # #     """
# # # # #     if payin is None or payin == 0:
# # # # #         return 0, "0% (No Payin)", "Payin is 0"
    
# # # # #     payin_cat = get_payin_category(payin)
    
# # # # #     if payin <= 20:
# # # # #         deduction = 2
# # # # #     elif payin <= 30:
# # # # #         deduction = 3
# # # # #     elif payin <= 50:
# # # # #         deduction = 4
# # # # #     else:
# # # # #         deduction = 5
    
# # # # #     payout = round(payin - deduction, 2)
# # # # #     formula = f"-{deduction}%"
# # # # #     explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
# # # # #     return payout, formula, explanation


# # # # # # ===============================================================================
# # # # # # PATTERN DETECTION
# # # # # # ===============================================================================

# # # # # class CVPatternDetector:
# # # # #     """Detect CV pattern type."""
    
# # # # #     @staticmethod
# # # # #     def detect_pattern(df: pd.DataFrame) -> str:
# # # # #         """
# # # # #         Detect pattern:
# # # # #         - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
# # # # #         - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
# # # # #         """
# # # # #         sample_text = ""
# # # # #         for i in range(min(10, df.shape[0])):
# # # # #             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # # #             sample_text += row_text + " "
        
# # # # #         # Check for CV SATP
# # # # #         if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
# # # # #            ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
# # # # #             return "cv_satp"
        
# # # # #         # Check for CV COMP
# # # # #         if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
# # # # #            ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
# # # # #             return "cv_comp"
        
# # # # #         # Default
# # # # #         return "cv_comp"


# # # # # # ===============================================================================
# # # # # # CV COMP PROCESSOR
# # # # # # ===============================================================================

# # # # # class CVCompProcessor:
# # # # #     """Process CV COMP sheets."""
    
# # # # #     @staticmethod
# # # # #     def process(content: bytes, sheet_name: str,
# # # # #                 override_enabled: bool = False,
# # # # #                 override_lob: str = None,
# # # # #                 override_segment: str = None) -> List[Dict]:
# # # # #         """
# # # # #         Process CV COMP pattern:
# # # # #         Row 1: Title (JAN 2025 CV)
# # # # #         Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
# # # # #         Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
# # # # #         Row 5+: Data rows
# # # # #         """
# # # # #         records = []
        
# # # # #         try:
# # # # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # # # #             print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
# # # # #             print(f"[CV_COMP] Sheet shape: {df.shape}")
            
# # # # #             # Find header row with "Geo Segments"
# # # # #             header_row = None
# # # # #             for i in range(min(10, df.shape[0])):
# # # # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # # #                 if "GEO SEGMENT" in row_text:
# # # # #                     header_row = i
# # # # #                     break
            
# # # # #             if header_row is None:
# # # # #                 print("[CV_COMP] Header row not found")
# # # # #                 return records
            
# # # # #             print(f"[CV_COMP] Found header row at index: {header_row}")
            
# # # # #             # Next row might have age bands (New, >1-5 Years, etc.)
# # # # #             age_row = header_row + 1
            
# # # # #             # Data starts after age row
# # # # #             data_start = age_row + 1
# # # # #             for i in range(data_start, df.shape[0]):
# # # # #                 if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
# # # # #                     data_start = i
# # # # #                     break
            
# # # # #             print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
# # # # #             # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
# # # # #             col_meta = []
# # # # #             for col_idx in range(2, df.shape[1]):
# # # # #                 tonnage = cell_to_str(df.iloc[header_row, col_idx])
# # # # #                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
# # # # #                 if not tonnage and not age_band:
# # # # #                     continue
                
# # # # #                 # Build segment description
# # # # #                 segment_desc = ""
# # # # #                 if tonnage:
# # # # #                     segment_desc = tonnage
# # # # #                 if age_band:
# # # # #                     segment_desc += f" ({age_band})" if segment_desc else age_band
                
# # # # #                 col_meta.append({
# # # # #                     "col_idx": col_idx,
# # # # #                     "tonnage": tonnage,
# # # # #                     "age_band": age_band,
# # # # #                     "segment_desc": segment_desc,
# # # # #                 })
            
# # # # #             if not col_meta:
# # # # #                 print("[CV_COMP] No data columns found")
# # # # #                 return records
            
# # # # #             print(f"[CV_COMP] Found {len(col_meta)} columns")
# # # # #             for m in col_meta[:5]:
# # # # #                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
# # # # #             # Process data rows
# # # # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # # # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # # # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # # # #             for row_idx in range(data_start, df.shape[0]):
# # # # #                 geo_segments = cell_to_str(df.iloc[row_idx, 0])
# # # # #                 geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
# # # # #                 if not geo_segments and not geo_segment_cv:
# # # # #                     continue
                
# # # # #                 if geo_segments.lower() in skip_words:
# # # # #                     continue
                
# # # # #                 # Combine both geo columns
# # # # #                 combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
# # # # #                 # Extract state
# # # # #                 state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
# # # # #                 # Process each column
# # # # #                 for m in col_meta:
# # # # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # # # #                     if payin is None or payin == 0:
# # # # #                         continue
                    
# # # # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # # # #                     records.append({
# # # # #                         "State": state,
# # # # #                         "Geo Location": combined_location,
# # # # #                         "Geo Segments": geo_segments,
# # # # #                         "Geo Segment CV": geo_segment_cv,
# # # # #                         "Original Segment": m["segment_desc"],
# # # # #                         "Tonnage": m["tonnage"],
# # # # #                         "Age Band": m["age_band"],
# # # # #                         "Mapped Segment": segment_final,
# # # # #                         "LOB": lob_final,
# # # # #                         "Status": "STP",
# # # # #                         "Payin": f"{payin:.2f}%",
# # # # #                         "Payin Category": get_payin_category(payin),
# # # # #                         "Calculated Payout": f"{payout:.2f}%",
# # # # #                         "Formula Used": formula,
# # # # #                         "Rule Explanation": explanation,
# # # # #                     })
            
# # # # #             print(f"[CV_COMP] Extracted {len(records)} records")
# # # # #             return records
            
# # # # #         except Exception as e:
# # # # #             print(f"[CV_COMP] Error: {e}")
# # # # #             traceback.print_exc()
# # # # #             return []


# # # # # # ===============================================================================
# # # # # # CV SATP PROCESSOR
# # # # # # ===============================================================================

# # # # # class CVSATPProcessor:
# # # # #     """Process CV SATP sheets."""
    
# # # # #     @staticmethod
# # # # #     def process(content: bytes, sheet_name: str,
# # # # #                 override_enabled: bool = False,
# # # # #                 override_lob: str = None,
# # # # #                 override_segment: str = None) -> List[Dict]:
# # # # #         """
# # # # #         Process CV SATP pattern:
# # # # #         Row 1: Title (JAN 2025 PAYOUT_CV SATP)
# # # # #         Row 2: Segment (tonnage categories)
# # # # #         Row 3: Geo Location - New
# # # # #         Row 5+: Data rows
# # # # #         """
# # # # #         records = []
        
# # # # #         try:
# # # # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # # # #             print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
# # # # #             print(f"[CV_SATP] Sheet shape: {df.shape}")
            
# # # # #             # Find segment row (tonnage categories)
# # # # #             segment_row = None
# # # # #             for i in range(min(10, df.shape[0])):
# # # # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # # #                 if "SEGMENT" in row_text and ("TON" in row_text or "GCV" in row_text or "PCV" in row_text):
# # # # #                     segment_row = i
# # # # #                     break
            
# # # # #             if segment_row is None:
# # # # #                 print("[CV_SATP] Segment row not found")
# # # # #                 return records
            
# # # # #             print(f"[CV_SATP] Found segment row at index: {segment_row}")
            
# # # # #             # Next row is Geo Location row
# # # # #             geo_header_row = segment_row + 1
            
# # # # #             # Data starts after geo header
# # # # #             data_start = geo_header_row + 1
# # # # #             for i in range(data_start, df.shape[0]):
# # # # #                 if cell_to_str(df.iloc[i, 0]):
# # # # #                     data_start = i
# # # # #                     break
            
# # # # #             print(f"[CV_SATP] Geo header row: {geo_header_row}, Data starts: {data_start}")
            
# # # # #             # Build column metadata (column 0 is Geo Location - New)
# # # # #             col_meta = []
# # # # #             for col_idx in range(1, df.shape[1]):
# # # # #                 segment = cell_to_str(df.iloc[segment_row, col_idx])
                
# # # # #                 if not segment:
# # # # #                     continue
                
# # # # #                 # Skip if it's a header label
# # # # #                 if "GEO LOCATION" in segment.upper():
# # # # #                     continue
                
# # # # #                 col_meta.append({
# # # # #                     "col_idx": col_idx,
# # # # #                     "segment": segment,
# # # # #                 })
            
# # # # #             if not col_meta:
# # # # #                 print("[CV_SATP] No data columns found")
# # # # #                 return records
            
# # # # #             print(f"[CV_SATP] Found {len(col_meta)} columns")
# # # # #             for m in col_meta[:5]:
# # # # #                 print(f"  - Col {m['col_idx']}: {m['segment']}")
            
# # # # #             # Process data rows
# # # # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # # # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # # # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # # # #             for row_idx in range(data_start, df.shape[0]):
# # # # #                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
# # # # #                 if not geo_location or geo_location.lower() in skip_words:
# # # # #                     continue
                
# # # # #                 state = map_state(geo_location)
                
# # # # #                 # Process each column
# # # # #                 for m in col_meta:
# # # # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # # # #                     if payin is None or payin == 0:
# # # # #                         continue
                    
# # # # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # # # #                     records.append({
# # # # #                         "State": state,
# # # # #                         "Geo Location": geo_location,
# # # # #                         "Original Segment": m["segment"],
# # # # #                         "Mapped Segment": segment_final,
# # # # #                         "LOB": lob_final,
# # # # #                         "Status": "STP",
# # # # #                         "Payin": f"{payin:.2f}%",
# # # # #                         "Payin Category": get_payin_category(payin),
# # # # #                         "Calculated Payout": f"{payout:.2f}%",
# # # # #                         "Formula Used": formula,
# # # # #                         "Rule Explanation": explanation,
# # # # #                     })
            
# # # # #             print(f"[CV_SATP] Extracted {len(records)} records")
# # # # #             return records
            
# # # # #         except Exception as e:
# # # # #             print(f"[CV_SATP] Error: {e}")
# # # # #             traceback.print_exc()
# # # # #             return []


# # # # # # ===============================================================================
# # # # # # PATTERN DISPATCHER
# # # # # # ===============================================================================

# # # # # class CVPatternDispatcher:
# # # # #     """Route to correct CV processor."""
    
# # # # #     PATTERN_PROCESSORS = {
# # # # #         "cv_comp": CVCompProcessor,
# # # # #         "cv_satp": CVSATPProcessor,
# # # # #     }
    
# # # # #     @staticmethod
# # # # #     def process_sheet(content: bytes, sheet_name: str,
# # # # #                       override_enabled: bool = False,
# # # # #                       override_lob: str = None,
# # # # #                       override_segment: str = None) -> List[Dict]:
# # # # #         """Detect pattern and route to processor."""
# # # # #         df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
# # # # #         pattern = CVPatternDetector.detect_pattern(df_raw)
        
# # # # #         print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
# # # # #         processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
# # # # #         return processor_class.process(
# # # # #             content, sheet_name,
# # # # #             override_enabled, override_lob, override_segment
# # # # #         )


# # # # # # ===============================================================================
# # # # # # API ENDPOINTS
# # # # # # ===============================================================================

# # # # # @app.get("/")
# # # # # async def root():
# # # # #     return {
# # # # #         "message": "Carrying Vehicles Payout Processor API",
# # # # #         "version": "1.0.0",
# # # # #         "formula": "Tiered deduction based on payin ranges (independent of policy type)",
# # # # #         "supported_lobs": ["CV"],
# # # # #         "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
# # # # #         "supported_patterns": [
# # # # #             "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
# # # # #             "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)"
# # # # #         ],
# # # # #         "formula_tiers": [
# # # # #             "Payin ≤ 20%: -2%",
# # # # #             "Payin 21-30%: -3%",
# # # # #             "Payin 31-50%: -4%",
# # # # #             "Payin > 50%: -5%"
# # # # #         ]
# # # # #     }


# # # # # @app.post("/upload")
# # # # # async def upload_file(file: UploadFile = File(...)):
# # # # #     """Upload Excel file."""
# # # # #     try:
# # # # #         if not file.filename.endswith((".xlsx", ".xls")):
# # # # #             raise HTTPException(status_code=400, detail="Only Excel files supported")
        
# # # # #         content = await file.read()
# # # # #         xls = pd.ExcelFile(io.BytesIO(content))
# # # # #         sheets = xls.sheet_names
        
# # # # #         file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
# # # # #         uploaded_files[file_id] = {
# # # # #             "content": content,
# # # # #             "filename": file.filename,
# # # # #             "sheets": sheets,
# # # # #         }
        
# # # # #         return {
# # # # #             "file_id": file_id,
# # # # #             "filename": file.filename,
# # # # #             "sheets": sheets,
# # # # #             "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
# # # # #         }
        
# # # # #     except Exception as e:
# # # # #         raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


# # # # # @app.post("/process")
# # # # # async def process_sheet(
# # # # #     file_id: str,
# # # # #     sheet_name: str,
# # # # #     override_enabled: bool = False,
# # # # #     override_lob: Optional[str] = None,
# # # # #     override_segment: Optional[str] = None,
# # # # # ):
# # # # #     """Process worksheet."""
# # # # #     try:
# # # # #         if file_id not in uploaded_files:
# # # # #             raise HTTPException(status_code=404, detail="File not found")
        
# # # # #         file_data = uploaded_files[file_id]
        
# # # # #         if sheet_name not in file_data["sheets"]:
# # # # #             raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
# # # # #         records = CVPatternDispatcher.process_sheet(
# # # # #             file_data["content"], 
# # # # #             sheet_name,
# # # # #             override_enabled, 
# # # # #             override_lob, 
# # # # #             override_segment,
# # # # #         )
        
# # # # #         if not records:
# # # # #             return {
# # # # #                 "success": False,
# # # # #                 "message": "No records extracted. Check sheet structure.",
# # # # #                 "records": [],
# # # # #                 "count": 0,
# # # # #             }
        
# # # # #         # Summary stats
# # # # #         states = {}
# # # # #         payins = []
# # # # #         payouts = []
        
# # # # #         for r in records:
# # # # #             state = r.get("State", "UNKNOWN")
# # # # #             states[state] = states.get(state, 0) + 1
            
# # # # #             try:
# # # # #                 payin_val = float(r.get("Payin", "0%").replace("%", ""))
# # # # #                 payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
# # # # #                 payins.append(payin_val)
# # # # #                 payouts.append(payout_val)
# # # # #             except Exception:
# # # # #                 pass
        
# # # # #         avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
# # # # #         avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
# # # # #         return {
# # # # #             "success": True,
# # # # #             "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
# # # # #             "records": records,
# # # # #             "count": len(records),
# # # # #             "summary": {
# # # # #                 "total_records": len(records),
# # # # #                 "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
# # # # #                 "average_payin": avg_payin,
# # # # #                 "average_payout": avg_payout,
# # # # #             },
# # # # #         }
        
# # # # #     except Exception as e:
# # # # #         traceback.print_exc()
# # # # #         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


# # # # # @app.post("/export")
# # # # # async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
# # # # #     """Export to Excel."""
# # # # #     try:
# # # # #         if not records:
# # # # #             raise HTTPException(status_code=400, detail="No records to export")
        
# # # # #         df = pd.DataFrame(records)
        
# # # # #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # # # #         filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
# # # # #         out_path = os.path.join(tempfile.gettempdir(), filename)
        
# # # # #         with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
# # # # #             df.to_excel(writer, index=False, sheet_name="Processed Data")
            
# # # # #             worksheet = writer.sheets["Processed Data"]
# # # # #             for idx, col in enumerate(df.columns):
# # # # #                 max_length = max(
# # # # #                     df[col].astype(str).apply(len).max(),
# # # # #                     len(str(col))
# # # # #                 )
# # # # #                 worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
# # # # #         return FileResponse(
# # # # #             path=out_path,
# # # # #             filename=filename,
# # # # #             media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
# # # # #         )
        
# # # # #     except Exception as e:
# # # # #         raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


# # # # # @app.get("/health")
# # # # # async def health_check():
# # # # #     """Health check."""
# # # # #     return {
# # # # #         "status": "healthy",
# # # # #         "timestamp": datetime.now().isoformat(),
# # # # #         "uploaded_files": len(uploaded_files)
# # # # #     }


# # # # # if __name__ == "__main__":
# # # # #     import uvicorn
# # # # #     print("\n" + "=" * 70)
# # # # #     print("Carrying Vehicles Payout Processor API - v1.0.0")
# # # # #     print("Patterns: CV COMP + CV SATP")
# # # # #     print("Formula: Independent of policy type, tiered deductions")
# # # # #     print("=" * 70 + "\n")
# # # # #     uvicorn.run(app, host="0.0.0.0", port=8000)

# # # # from fastapi import FastAPI, File, UploadFile, HTTPException
# # # # from fastapi.middleware.cors import CORSMiddleware
# # # # from fastapi.responses import FileResponse, JSONResponse
# # # # import pandas as pd
# # # # import io
# # # # import os
# # # # from typing import List, Dict, Tuple, Optional
# # # # from datetime import datetime
# # # # import traceback
# # # # import tempfile

# # # # app = FastAPI(title="Carrying Vehicles Payout Processor API")

# # # # app.add_middleware(
# # # #     CORSMiddleware,
# # # #     allow_origins=["*"],  
# # # #     allow_credentials=True,
# # # #     allow_methods=["*"],
# # # #     allow_headers=["*"],
# # # # )

# # # # # ===============================================================================
# # # # # FORMULA DATA
# # # # # ===============================================================================
# # # # FORMULA_DATA = [
# # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
# # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
# # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
# # # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# # # # ]

# # # # # ===============================================================================
# # # # # STATE MAPPING
# # # # # ===============================================================================
# # # # STATE_MAPPING = {
# # # #     "ANDHRA PRADESH": "ANDHRA PRADESH",
# # # #     "KRISHNA": "ANDHRA PRADESH",
# # # #     "VIJAYWADA": "ANDHRA PRADESH",
# # # #     "VIJAYAWADA": "ANDHRA PRADESH",
# # # #     "VISAKHAPATNAM": "ANDHRA PRADESH",
    
# # # #     "KARNATAKA": "KARNATAKA",
# # # #     "BANGALORE": "KARNATAKA",
# # # #     "BENGALURU": "KARNATAKA",
    
# # # #     "KERALA": "KERALA",
# # # #     "ERNAKULAM": "KERALA",
# # # #     "COCHIN": "KERALA",
    
# # # #     "TAMIL NADU": "TAMIL NADU",
# # # #     "CHENNAI": "TAMIL NADU",
# # # #     "PONDICHERRY": "TAMIL NADU",
    
# # # #     "TELANGANA": "TELANGANA",
# # # #     "HYDERABAD": "TELANGANA",
    
# # # #     "MAHARASHTRA": "MAHARASHTRA",
# # # #     "MUMBAI": "MAHARASHTRA",
# # # #     "PUNE": "MAHARASHTRA",
# # # #     "NAGPUR": "MAHARASHTRA",
    
# # # #     "MADHYA PRADESH": "MADHYA PRADESH",
# # # #     "BHOPAL": "MADHYA PRADESH",
# # # #     "GWALIOR": "MADHYA PRADESH",
# # # #     "JABALPUR": "MADHYA PRADESH",
    
# # # #     "CHANDIGARH": "CHANDIGARH",
# # # #     "DELHI": "DELHI",
# # # #     "NCR": "DELHI",
# # # #     "GOA": "GOA",
    
# # # #     "HIMACHAL PRADESH": "HIMACHAL PRADESH",
# # # #     "BILASPUR": "HIMACHAL PRADESH",
# # # #     "MANDI": "HIMACHAL PRADESH",
# # # #     "SOLAN": "HIMACHAL PRADESH",
# # # #     "SHIMLA": "HIMACHAL PRADESH",
# # # #     "MANALI": "HIMACHAL PRADESH",
# # # # }

# # # # uploaded_files = {}

# # # # # ===============================================================================
# # # # # HELPER FUNCTIONS
# # # # # ===============================================================================

# # # # def cell_to_str(val) -> str:
# # # #     """Safely convert ANY cell value to string."""
# # # #     if val is None:
# # # #         return ""
# # # #     try:
# # # #         if pd.isna(val):
# # # #             return ""
# # # #     except (TypeError, ValueError):
# # # #         pass
# # # #     return str(val).strip()


# # # # def safe_float(value) -> Optional[float]:
# # # #     """Safely convert value to float, handling percentages."""
# # # #     if value is None:
# # # #         return None
# # # #     try:
# # # #         if pd.isna(value):
# # # #             return None
# # # #     except (TypeError, ValueError):
# # # #         pass
    
# # # #     s = str(value).strip().upper().replace("%", "")
# # # #     if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
# # # #         return None
    
# # # #     try:
# # # #         num = float(s)
# # # #         if num < 0:
# # # #             return None
# # # #         return num * 100 if 0 < num < 1 else num
# # # #     except Exception:
# # # #         return None


# # # # def map_state(location: str) -> str:
# # # #     """Map location to state."""
# # # #     location_upper = location.upper()
    
# # # #     for key, val in STATE_MAPPING.items():
# # # #         if key.upper() in location_upper:
# # # #             return val
    
# # # #     return location


# # # # def get_payin_category(payin: float) -> str:
# # # #     """Get payin category."""
# # # #     if payin <= 20:
# # # #         return "Payin Below 20%"
# # # #     elif payin <= 30:
# # # #         return "Payin 21% to 30%"
# # # #     elif payin <= 50:
# # # #         return "Payin 31% to 50%"
# # # #     else:
# # # #         return "Payin Above 50%"


# # # # def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
# # # #     """
# # # #     Calculate payout for CV based on payin ranges.
# # # #     CV is independent of policy type - uses tiered deductions.
# # # #     """
# # # #     if payin is None or payin == 0:
# # # #         return 0, "0% (No Payin)", "Payin is 0"
    
# # # #     payin_cat = get_payin_category(payin)
    
# # # #     if payin <= 20:
# # # #         deduction = 2
# # # #     elif payin <= 30:
# # # #         deduction = 3
# # # #     elif payin <= 50:
# # # #         deduction = 4
# # # #     else:
# # # #         deduction = 5
    
# # # #     payout = round(payin - deduction, 2)
# # # #     formula = f"-{deduction}%"
# # # #     explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
# # # #     return payout, formula, explanation


# # # # # ===============================================================================
# # # # # PATTERN DETECTION
# # # # # ===============================================================================

# # # # class CVPatternDetector:
# # # #     """Detect CV pattern type."""
    
# # # #     @staticmethod
# # # #     def detect_pattern(df: pd.DataFrame) -> str:
# # # #         """
# # # #         Detect pattern:
# # # #         - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
# # # #         - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
# # # #         """
# # # #         sample_text = ""
# # # #         for i in range(min(10, df.shape[0])):
# # # #             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # #             sample_text += row_text + " "
        
# # # #         # Check for CV SATP
# # # #         if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
# # # #            ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
# # # #             return "cv_satp"
        
# # # #         # Check for CV COMP
# # # #         if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
# # # #            ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
# # # #             return "cv_comp"
        
# # # #         # Default
# # # #         return "cv_comp"


# # # # # ===============================================================================
# # # # # CV COMP PROCESSOR
# # # # # ===============================================================================

# # # # class CVCompProcessor:
# # # #     """Process CV COMP sheets."""
    
# # # #     @staticmethod
# # # #     def process(content: bytes, sheet_name: str,
# # # #                 override_enabled: bool = False,
# # # #                 override_lob: str = None,
# # # #                 override_segment: str = None) -> List[Dict]:
# # # #         """
# # # #         Process CV COMP pattern:
# # # #         Row 1: Title (JAN 2025 CV)
# # # #         Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
# # # #         Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
# # # #         Row 5+: Data rows
# # # #         """
# # # #         records = []
        
# # # #         try:
# # # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # # #             print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
# # # #             print(f"[CV_COMP] Sheet shape: {df.shape}")
            
# # # #             # Find header row with "Geo Segments"
# # # #             header_row = None
# # # #             for i in range(min(10, df.shape[0])):
# # # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # #                 if "GEO SEGMENT" in row_text:
# # # #                     header_row = i
# # # #                     break
            
# # # #             if header_row is None:
# # # #                 print("[CV_COMP] Header row not found")
# # # #                 return records
            
# # # #             print(f"[CV_COMP] Found header row at index: {header_row}")
            
# # # #             # Next row might have age bands (New, >1-5 Years, etc.)
# # # #             age_row = header_row + 1
            
# # # #             # Data starts after age row
# # # #             data_start = age_row + 1
# # # #             for i in range(data_start, df.shape[0]):
# # # #                 if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
# # # #                     data_start = i
# # # #                     break
            
# # # #             print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
# # # #             # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
# # # #             col_meta = []
# # # #             for col_idx in range(2, df.shape[1]):
# # # #                 tonnage = cell_to_str(df.iloc[header_row, col_idx])
# # # #                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
# # # #                 if not tonnage and not age_band:
# # # #                     continue
                
# # # #                 # Build segment description
# # # #                 segment_desc = ""
# # # #                 if tonnage:
# # # #                     segment_desc = tonnage
# # # #                 if age_band:
# # # #                     segment_desc += f" ({age_band})" if segment_desc else age_band
                
# # # #                 col_meta.append({
# # # #                     "col_idx": col_idx,
# # # #                     "tonnage": tonnage,
# # # #                     "age_band": age_band,
# # # #                     "segment_desc": segment_desc,
# # # #                 })
            
# # # #             if not col_meta:
# # # #                 print("[CV_COMP] No data columns found")
# # # #                 return records
            
# # # #             print(f"[CV_COMP] Found {len(col_meta)} columns")
# # # #             for m in col_meta[:5]:
# # # #                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
# # # #             # Process data rows
# # # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # # #             for row_idx in range(data_start, df.shape[0]):
# # # #                 geo_segments = cell_to_str(df.iloc[row_idx, 0])
# # # #                 geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
# # # #                 if not geo_segments and not geo_segment_cv:
# # # #                     continue
                
# # # #                 if geo_segments.lower() in skip_words:
# # # #                     continue
                
# # # #                 # Combine both geo columns
# # # #                 combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
# # # #                 # Extract state
# # # #                 state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
# # # #                 # Process each column
# # # #                 for m in col_meta:
# # # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # # #                     if payin is None or payin == 0:
# # # #                         continue
                    
# # # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # # #                     records.append({
# # # #                         "State": state,
# # # #                         "Geo Location": combined_location,
# # # #                         "Geo Segments": geo_segments,
# # # #                         "Geo Segment CV": geo_segment_cv,
# # # #                         "Original Segment": m["segment_desc"],
# # # #                         "Tonnage": m["tonnage"],
# # # #                         "Age Band": m["age_band"],
# # # #                         "Mapped Segment": segment_final,
# # # #                         "LOB": lob_final,
# # # #                         "Status": "STP",
# # # #                         "Payin": f"{payin:.2f}%",
# # # #                         "Payin Category": get_payin_category(payin),
# # # #                         "Calculated Payout": f"{payout:.2f}%",
# # # #                         "Formula Used": formula,
# # # #                         "Rule Explanation": explanation,
# # # #                     })
            
# # # #             print(f"[CV_COMP] Extracted {len(records)} records")
# # # #             return records
            
# # # #         except Exception as e:
# # # #             print(f"[CV_COMP] Error: {e}")
# # # #             traceback.print_exc()
# # # #             return []


# # # # # ===============================================================================
# # # # # CV SATP PROCESSOR
# # # # # ===============================================================================

# # # # class CVSATPProcessor:
# # # #     """Process CV SATP sheets."""
    
# # # #     @staticmethod
# # # #     def process(content: bytes, sheet_name: str,
# # # #                 override_enabled: bool = False,
# # # #                 override_lob: str = None,
# # # #                 override_segment: str = None) -> List[Dict]:
# # # #         """
# # # #         Process CV SATP pattern:
# # # #         Row 1: Title (JAN 2025 PAYOUT_CV SATP)
# # # #         Row 2: Segment
# # # #         Row 3: Geo Location - New | Upto 2.5 Ton GCV 4W GCV 3W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
# # # #         Row 5+: Data rows
# # # #         """
# # # #         records = []
        
# # # #         try:
# # # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # # #             print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
# # # #             print(f"[CV_SATP] Sheet shape: {df.shape}")
            
# # # #             # Find the row with tonnage categories (GCV, PCV, Ton, etc.)
# # # #             tonnage_row = None
# # # #             for i in range(min(10, df.shape[0])):
# # # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # # #                 if ("TON" in row_text or "GCV" in row_text or "PCV" in row_text or "AUTORICKSHAW" in row_text) and \
# # # #                    "GEO LOCATION" in row_text:
# # # #                     tonnage_row = i
# # # #                     break
            
# # # #             # Alternative: look for row with "Geo Location - New" in first column
# # # #             if tonnage_row is None:
# # # #                 for i in range(min(10, df.shape[0])):
# # # #                     cell = cell_to_str(df.iloc[i, 0]).upper()
# # # #                     if "GEO LOCATION" in cell and "NEW" in cell:
# # # #                         tonnage_row = i
# # # #                         break
            
# # # #             if tonnage_row is None:
# # # #                 print("[CV_SATP] Tonnage row not found")
# # # #                 print("[CV_SATP] First 10 rows:")
# # # #                 for i in range(min(10, df.shape[0])):
# # # #                     print(f"  Row {i}: {[cell_to_str(df.iloc[i, j]) for j in range(min(6, df.shape[1]))]}")
# # # #                 return records
            
# # # #             print(f"[CV_SATP] Found tonnage row at index: {tonnage_row}")
            
# # # #             # Data starts after tonnage row, skip empty rows
# # # #             data_start = tonnage_row + 1
# # # #             for i in range(data_start, df.shape[0]):
# # # #                 if cell_to_str(df.iloc[i, 0]):
# # # #                     data_start = i
# # # #                     break
            
# # # #             print(f"[CV_SATP] Data starts: {data_start}")
            
# # # #             # Build column metadata (column 0 is Geo Location - New)
# # # #             col_meta = []
# # # #             for col_idx in range(1, df.shape[1]):
# # # #                 segment = cell_to_str(df.iloc[tonnage_row, col_idx])
                
# # # #                 if not segment:
# # # #                     continue
                
# # # #                 # Skip if it's empty or just whitespace
# # # #                 if segment.strip() == "":
# # # #                     continue
                
# # # #                 col_meta.append({
# # # #                     "col_idx": col_idx,
# # # #                     "segment": segment,
# # # #                 })
            
# # # #             if not col_meta:
# # # #                 print("[CV_SATP] No data columns found")
# # # #                 print(f"[CV_SATP] Tonnage row content: {[cell_to_str(df.iloc[tonnage_row, i]) for i in range(df.shape[1])]}")
# # # #                 return records
            
# # # #             print(f"[CV_SATP] Found {len(col_meta)} columns")
# # # #             for m in col_meta:
# # # #                 print(f"  - Col {m['col_idx']}: {m['segment']}")
            
# # # #             # Process data rows
# # # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # # #             for row_idx in range(data_start, df.shape[0]):
# # # #                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
# # # #                 if not geo_location or geo_location.lower() in skip_words:
# # # #                     continue
                
# # # #                 state = map_state(geo_location)
                
# # # #                 # Process each column
# # # #                 for m in col_meta:
# # # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # # #                     if payin is None or payin == 0:
# # # #                         continue
                    
# # # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # # #                     records.append({
# # # #                         "State": state,
# # # #                         "Geo Location": geo_location,
# # # #                         "Original Segment": m["segment"],
# # # #                         "Mapped Segment": segment_final,
# # # #                         "LOB": lob_final,
# # # #                         "Status": "STP",
# # # #                         "Payin": f"{payin:.2f}%",
# # # #                         "Payin Category": get_payin_category(payin),
# # # #                         "Calculated Payout": f"{payout:.2f}%",
# # # #                         "Formula Used": formula,
# # # #                         "Rule Explanation": explanation,
# # # #                     })
            
# # # #             print(f"[CV_SATP] Extracted {len(records)} records")
# # # #             return records
            
# # # #         except Exception as e:
# # # #             print(f"[CV_SATP] Error: {e}")
# # # #             traceback.print_exc()
# # # #             return []


# # # # # ===============================================================================
# # # # # PATTERN DISPATCHER
# # # # # ===============================================================================

# # # # class CVPatternDispatcher:
# # # #     """Route to correct CV processor."""
    
# # # #     PATTERN_PROCESSORS = {
# # # #         "cv_comp": CVCompProcessor,
# # # #         "cv_satp": CVSATPProcessor,
# # # #     }
    
# # # #     @staticmethod
# # # #     def process_sheet(content: bytes, sheet_name: str,
# # # #                       override_enabled: bool = False,
# # # #                       override_lob: str = None,
# # # #                       override_segment: str = None) -> List[Dict]:
# # # #         """Detect pattern and route to processor."""
# # # #         df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
# # # #         pattern = CVPatternDetector.detect_pattern(df_raw)
        
# # # #         print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
# # # #         processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
# # # #         return processor_class.process(
# # # #             content, sheet_name,
# # # #             override_enabled, override_lob, override_segment
# # # #         )


# # # # # ===============================================================================
# # # # # API ENDPOINTS
# # # # # ===============================================================================

# # # # @app.get("/")
# # # # async def root():
# # # #     return {
# # # #         "message": "Carrying Vehicles Payout Processor API",
# # # #         "version": "1.0.0",
# # # #         "formula": "Tiered deduction based on payin ranges (independent of policy type)",
# # # #         "supported_lobs": ["CV"],
# # # #         "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
# # # #         "supported_patterns": [
# # # #             "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
# # # #             "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)"
# # # #         ],
# # # #         "formula_tiers": [
# # # #             "Payin ≤ 20%: -2%",
# # # #             "Payin 21-30%: -3%",
# # # #             "Payin 31-50%: -4%",
# # # #             "Payin > 50%: -5%"
# # # #         ]
# # # #     }


# # # # @app.post("/upload")
# # # # async def upload_file(file: UploadFile = File(...)):
# # # #     """Upload Excel file."""
# # # #     try:
# # # #         if not file.filename.endswith((".xlsx", ".xls")):
# # # #             raise HTTPException(status_code=400, detail="Only Excel files supported")
        
# # # #         content = await file.read()
# # # #         xls = pd.ExcelFile(io.BytesIO(content))
# # # #         sheets = xls.sheet_names
        
# # # #         file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
# # # #         uploaded_files[file_id] = {
# # # #             "content": content,
# # # #             "filename": file.filename,
# # # #             "sheets": sheets,
# # # #         }
        
# # # #         return {
# # # #             "file_id": file_id,
# # # #             "filename": file.filename,
# # # #             "sheets": sheets,
# # # #             "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
# # # #         }
        
# # # #     except Exception as e:
# # # #         raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


# # # # @app.post("/process")
# # # # async def process_sheet(
# # # #     file_id: str,
# # # #     sheet_name: str,
# # # #     override_enabled: bool = False,
# # # #     override_lob: Optional[str] = None,
# # # #     override_segment: Optional[str] = None,
# # # # ):
# # # #     """Process worksheet."""
# # # #     try:
# # # #         if file_id not in uploaded_files:
# # # #             raise HTTPException(status_code=404, detail="File not found")
        
# # # #         file_data = uploaded_files[file_id]
        
# # # #         if sheet_name not in file_data["sheets"]:
# # # #             raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
# # # #         records = CVPatternDispatcher.process_sheet(
# # # #             file_data["content"], 
# # # #             sheet_name,
# # # #             override_enabled, 
# # # #             override_lob, 
# # # #             override_segment,
# # # #         )
        
# # # #         if not records:
# # # #             return {
# # # #                 "success": False,
# # # #                 "message": "No records extracted. Check sheet structure.",
# # # #                 "records": [],
# # # #                 "count": 0,
# # # #             }
        
# # # #         # Summary stats
# # # #         states = {}
# # # #         payins = []
# # # #         payouts = []
        
# # # #         for r in records:
# # # #             state = r.get("State", "UNKNOWN")
# # # #             states[state] = states.get(state, 0) + 1
            
# # # #             try:
# # # #                 payin_val = float(r.get("Payin", "0%").replace("%", ""))
# # # #                 payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
# # # #                 payins.append(payin_val)
# # # #                 payouts.append(payout_val)
# # # #             except Exception:
# # # #                 pass
        
# # # #         avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
# # # #         avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
# # # #         return {
# # # #             "success": True,
# # # #             "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
# # # #             "records": records,
# # # #             "count": len(records),
# # # #             "summary": {
# # # #                 "total_records": len(records),
# # # #                 "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
# # # #                 "average_payin": avg_payin,
# # # #                 "average_payout": avg_payout,
# # # #             },
# # # #         }
        
# # # #     except Exception as e:
# # # #         traceback.print_exc()
# # # #         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


# # # # @app.post("/export")
# # # # async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
# # # #     """Export to Excel."""
# # # #     try:
# # # #         if not records:
# # # #             raise HTTPException(status_code=400, detail="No records to export")
        
# # # #         df = pd.DataFrame(records)
        
# # # #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # # #         filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
# # # #         out_path = os.path.join(tempfile.gettempdir(), filename)
        
# # # #         with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
# # # #             df.to_excel(writer, index=False, sheet_name="Processed Data")
            
# # # #             worksheet = writer.sheets["Processed Data"]
# # # #             for idx, col in enumerate(df.columns):
# # # #                 max_length = max(
# # # #                     df[col].astype(str).apply(len).max(),
# # # #                     len(str(col))
# # # #                 )
# # # #                 worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
# # # #         return FileResponse(
# # # #             path=out_path,
# # # #             filename=filename,
# # # #             media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
# # # #         )
        
# # # #     except Exception as e:
# # # #         raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


# # # # @app.get("/health")
# # # # async def health_check():
# # # #     """Health check."""
# # # #     return {
# # # #         "status": "healthy",
# # # #         "timestamp": datetime.now().isoformat(),
# # # #         "uploaded_files": len(uploaded_files)
# # # #     }


# # # # if __name__ == "__main__":
# # # #     import uvicorn
# # # #     print("\n" + "=" * 70)
# # # #     print("Carrying Vehicles Payout Processor API - v1.0.0")
# # # #     print("Patterns: CV COMP + CV SATP")
# # # #     print("Formula: Independent of policy type, tiered deductions")
# # # #     print("=" * 70 + "\n")
# # # #     uvicorn.run(app, host="0.0.0.0", port=8000)

# # # from fastapi import FastAPI, File, UploadFile, HTTPException
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from fastapi.responses import FileResponse, JSONResponse
# # # import pandas as pd
# # # import io
# # # import os
# # # from typing import List, Dict, Tuple, Optional
# # # from datetime import datetime
# # # import traceback
# # # import tempfile

# # # app = FastAPI(title="Carrying Vehicles Payout Processor API")

# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["*"],  
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # # ===============================================================================
# # # # FORMULA DATA
# # # # ===============================================================================
# # # FORMULA_DATA = [
# # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
# # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
# # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
# # #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# # # ]

# # # # ===============================================================================
# # # # STATE MAPPING
# # # # ===============================================================================
# # # STATE_MAPPING = {
# # #     "ANDHRA PRADESH": "ANDHRA PRADESH",
# # #     "KRISHNA": "ANDHRA PRADESH",
# # #     "VIJAYWADA": "ANDHRA PRADESH",
# # #     "VIJAYAWADA": "ANDHRA PRADESH",
# # #     "VISAKHAPATNAM": "ANDHRA PRADESH",
    
# # #     "KARNATAKA": "KARNATAKA",
# # #     "BANGALORE": "KARNATAKA",
# # #     "BENGALURU": "KARNATAKA",
    
# # #     "KERALA": "KERALA",
# # #     "ERNAKULAM": "KERALA",
# # #     "COCHIN": "KERALA",
    
# # #     "TAMIL NADU": "TAMIL NADU",
# # #     "CHENNAI": "TAMIL NADU",
# # #     "PONDICHERRY": "TAMIL NADU",
    
# # #     "TELANGANA": "TELANGANA",
# # #     "HYDERABAD": "TELANGANA",
    
# # #     "MAHARASHTRA": "MAHARASHTRA",
# # #     "MUMBAI": "MAHARASHTRA",
# # #     "PUNE": "MAHARASHTRA",
# # #     "NAGPUR": "MAHARASHTRA",
    
# # #     "MADHYA PRADESH": "MADHYA PRADESH",
# # #     "BHOPAL": "MADHYA PRADESH",
# # #     "GWALIOR": "MADHYA PRADESH",
# # #     "JABALPUR": "MADHYA PRADESH",
    
# # #     "CHANDIGARH": "CHANDIGARH",
# # #     "DELHI": "DELHI",
# # #     "NCR": "DELHI",
# # #     "GOA": "GOA",
    
# # #     "HIMACHAL PRADESH": "HIMACHAL PRADESH",
# # #     "BILASPUR": "HIMACHAL PRADESH",
# # #     "MANDI": "HIMACHAL PRADESH",
# # #     "SOLAN": "HIMACHAL PRADESH",
# # #     "SHIMLA": "HIMACHAL PRADESH",
# # #     "MANALI": "HIMACHAL PRADESH",
# # # }

# # # uploaded_files = {}

# # # # ===============================================================================
# # # # HELPER FUNCTIONS
# # # # ===============================================================================

# # # def cell_to_str(val) -> str:
# # #     """Safely convert ANY cell value to string."""
# # #     if val is None:
# # #         return ""
# # #     try:
# # #         if pd.isna(val):
# # #             return ""
# # #     except (TypeError, ValueError):
# # #         pass
# # #     return str(val).strip()


# # # def safe_float(value) -> Optional[float]:
# # #     """Safely convert value to float, handling percentages."""
# # #     if value is None:
# # #         return None
# # #     try:
# # #         if pd.isna(value):
# # #             return None
# # #     except (TypeError, ValueError):
# # #         pass
    
# # #     s = str(value).strip().upper().replace("%", "")
# # #     if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
# # #         return None
    
# # #     try:
# # #         num = float(s)
# # #         if num < 0:
# # #             return None
# # #         return num * 100 if 0 < num < 1 else num
# # #     except Exception:
# # #         return None


# # # def map_state(location: str) -> str:
# # #     """Map location to state."""
# # #     location_upper = location.upper()
    
# # #     for key, val in STATE_MAPPING.items():
# # #         if key.upper() in location_upper:
# # #             return val
    
# # #     return location


# # # def get_payin_category(payin: float) -> str:
# # #     """Get payin category."""
# # #     if payin <= 20:
# # #         return "Payin Below 20%"
# # #     elif payin <= 30:
# # #         return "Payin 21% to 30%"
# # #     elif payin <= 50:
# # #         return "Payin 31% to 50%"
# # #     else:
# # #         return "Payin Above 50%"


# # # def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
# # #     """
# # #     Calculate payout for CV based on payin ranges.
# # #     CV is independent of policy type - uses tiered deductions.
# # #     """
# # #     if payin is None or payin == 0:
# # #         return 0, "0% (No Payin)", "Payin is 0"
    
# # #     payin_cat = get_payin_category(payin)
    
# # #     if payin <= 20:
# # #         deduction = 2
# # #     elif payin <= 30:
# # #         deduction = 3
# # #     elif payin <= 50:
# # #         deduction = 4
# # #     else:
# # #         deduction = 5
    
# # #     payout = round(payin - deduction, 2)
# # #     formula = f"-{deduction}%"
# # #     explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
# # #     return payout, formula, explanation


# # # # ===============================================================================
# # # # PATTERN DETECTION
# # # # ===============================================================================

# # # class CVPatternDetector:
# # #     """Detect CV pattern type."""
    
# # #     @staticmethod
# # #     def detect_pattern(df: pd.DataFrame) -> str:
# # #         """
# # #         Detect pattern:
# # #         - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
# # #         - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
# # #         """
# # #         sample_text = ""
# # #         for i in range(min(10, df.shape[0])):
# # #             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # #             sample_text += row_text + " "
        
# # #         # Check for CV SATP
# # #         if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
# # #            ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
# # #             return "cv_satp"
        
# # #         # Check for CV COMP
# # #         if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
# # #            ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
# # #             return "cv_comp"
        
# # #         # Default
# # #         return "cv_comp"


# # # # ===============================================================================
# # # # CV COMP PROCESSOR
# # # # ===============================================================================

# # # class CVCompProcessor:
# # #     """Process CV COMP sheets."""
    
# # #     @staticmethod
# # #     def process(content: bytes, sheet_name: str,
# # #                 override_enabled: bool = False,
# # #                 override_lob: str = None,
# # #                 override_segment: str = None) -> List[Dict]:
# # #         """
# # #         Process CV COMP pattern:
# # #         Row 1: Title (JAN 2025 CV)
# # #         Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
# # #         Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
# # #         Row 5+: Data rows
# # #         """
# # #         records = []
        
# # #         try:
# # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # #             print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
# # #             print(f"[CV_COMP] Sheet shape: {df.shape}")
            
# # #             # Find header row with "Geo Segments"
# # #             header_row = None
# # #             for i in range(min(10, df.shape[0])):
# # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # #                 if "GEO SEGMENT" in row_text:
# # #                     header_row = i
# # #                     break
            
# # #             if header_row is None:
# # #                 print("[CV_COMP] Header row not found")
# # #                 return records
            
# # #             print(f"[CV_COMP] Found header row at index: {header_row}")
            
# # #             # Next row might have age bands (New, >1-5 Years, etc.)
# # #             age_row = header_row + 1
            
# # #             # Data starts after age row
# # #             data_start = age_row + 1
# # #             for i in range(data_start, df.shape[0]):
# # #                 if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
# # #                     data_start = i
# # #                     break
            
# # #             print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
# # #             # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
# # #             col_meta = []
# # #             for col_idx in range(2, df.shape[1]):
# # #                 tonnage = cell_to_str(df.iloc[header_row, col_idx])
# # #                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
# # #                 if not tonnage and not age_band:
# # #                     continue
                
# # #                 # Build segment description
# # #                 segment_desc = ""
# # #                 if tonnage:
# # #                     segment_desc = tonnage
# # #                 if age_band:
# # #                     segment_desc += f" ({age_band})" if segment_desc else age_band
                
# # #                 col_meta.append({
# # #                     "col_idx": col_idx,
# # #                     "tonnage": tonnage,
# # #                     "age_band": age_band,
# # #                     "segment_desc": segment_desc,
# # #                 })
            
# # #             if not col_meta:
# # #                 print("[CV_COMP] No data columns found")
# # #                 return records
            
# # #             print(f"[CV_COMP] Found {len(col_meta)} columns")
# # #             for m in col_meta[:5]:
# # #                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
# # #             # Process data rows
# # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # #             for row_idx in range(data_start, df.shape[0]):
# # #                 geo_segments = cell_to_str(df.iloc[row_idx, 0])
# # #                 geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
# # #                 if not geo_segments and not geo_segment_cv:
# # #                     continue
                
# # #                 if geo_segments.lower() in skip_words:
# # #                     continue
                
# # #                 # Combine both geo columns
# # #                 combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
# # #                 # Extract state
# # #                 state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
# # #                 # Process each column
# # #                 for m in col_meta:
# # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # #                     if payin is None or payin == 0:
# # #                         continue
                    
# # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # #                     records.append({
# # #                         "State": state,
# # #                         "Geo Location": combined_location,
# # #                         "Geo Segments": geo_segments,
# # #                         "Geo Segment CV": geo_segment_cv,
# # #                         "Original Segment": m["segment_desc"],
# # #                         "Tonnage": m["tonnage"],
# # #                         "Age Band": m["age_band"],
# # #                         "Mapped Segment": segment_final,
# # #                         "LOB": lob_final,
# # #                         "Status": "STP",
# # #                         "Payin": f"{payin:.2f}%",
# # #                         "Payin Category": get_payin_category(payin),
# # #                         "Calculated Payout": f"{payout:.2f}%",
# # #                         "Formula Used": formula,
# # #                         "Rule Explanation": explanation,
# # #                     })
            
# # #             print(f"[CV_COMP] Extracted {len(records)} records")
# # #             return records
            
# # #         except Exception as e:
# # #             print(f"[CV_COMP] Error: {e}")
# # #             traceback.print_exc()
# # #             return []


# # # # ===============================================================================
# # # # CV SATP PROCESSOR
# # # # ===============================================================================

# # # class CVSATPProcessor:
# # #     """Process CV SATP sheets."""
    
# # #     @staticmethod
# # #     def process(content: bytes, sheet_name: str,
# # #                 override_enabled: bool = False,
# # #                 override_lob: str = None,
# # #                 override_segment: str = None) -> List[Dict]:
# # #         """
# # #         Process CV SATP pattern:
# # #         Row 1: Title (JAN 2025 PAYOUT_CV SATP)
# # #         Row 2: Segment | Upto 2.5 Ton GCV 4W GCV 3W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
# # #         Row 3: Geo Location - New | (empty or merged)
# # #         Row 5+: Data rows
# # #         """
# # #         records = []
        
# # #         try:
# # #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# # #             print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
# # #             print(f"[CV_SATP] Sheet shape: {df.shape}")
            
# # #             # Find the "Segment" row (contains tonnage categories)
# # #             segment_row = None
# # #             geo_row = None
            
# # #             for i in range(min(10, df.shape[0])):
# # #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# # #                 first_cell = cell_to_str(df.iloc[i, 0]).upper()
                
# # #                 # Row with "SEGMENT" in first column and tonnage in other columns
# # #                 if "SEGMENT" in first_cell and ("TON" in row_text or "GCV" in row_text or "PCV" in row_text):
# # #                     segment_row = i
# # #                     print(f"[CV_SATP] Found segment row at index: {i}")
                
# # #                 # Row with "GEO LOCATION" in first column
# # #                 if "GEO LOCATION" in first_cell:
# # #                     geo_row = i
# # #                     print(f"[CV_SATP] Found geo row at index: {i}")
            
# # #             if segment_row is None:
# # #                 print("[CV_SATP] Segment row not found")
# # #                 print("[CV_SATP] First 10 rows:")
# # #                 for i in range(min(10, df.shape[0])):
# # #                     print(f"  Row {i} Col 0: '{cell_to_str(df.iloc[i, 0])}'")
# # #                     if df.shape[1] > 1:
# # #                         print(f"    Col 1: '{cell_to_str(df.iloc[i, 1])}'")
# # #                 return records
            
# # #             print(f"[CV_SATP] Using segment row: {segment_row}")
            
# # #             # Data starts after geo_row (or segment_row + 1 if no geo_row found)
# # #             if geo_row is not None:
# # #                 data_start = geo_row + 1
# # #             else:
# # #                 data_start = segment_row + 1
            
# # #             # Skip empty rows
# # #             for i in range(data_start, df.shape[0]):
# # #                 if cell_to_str(df.iloc[i, 0]):
# # #                     data_start = i
# # #                     break
            
# # #             print(f"[CV_SATP] Data starts at row: {data_start}")
            
# # #             # Build column metadata from segment row (skip column 0 which is "Segment" label)
# # #             col_meta = []
# # #             for col_idx in range(1, df.shape[1]):
# # #                 segment = cell_to_str(df.iloc[segment_row, col_idx])
                
# # #                 if not segment or segment.strip() == "":
# # #                     continue
                
# # #                 col_meta.append({
# # #                     "col_idx": col_idx,
# # #                     "segment": segment,
# # #                 })
            
# # #             if not col_meta:
# # #                 print("[CV_SATP] No data columns found")
# # #                 print(f"[CV_SATP] Segment row content:")
# # #                 for col_idx in range(df.shape[1]):
# # #                     print(f"  Col {col_idx}: '{cell_to_str(df.iloc[segment_row, col_idx])}'")
# # #                 return records
            
# # #             print(f"[CV_SATP] Found {len(col_meta)} columns:")
# # #             for m in col_meta:
# # #                 print(f"  - Col {m['col_idx']}: '{m['segment']}'")
            
# # #             # Process data rows
# # #             lob_final = override_lob if override_enabled and override_lob else "CV"
# # #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# # #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# # #             processed_count = 0
# # #             for row_idx in range(data_start, df.shape[0]):
# # #                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
# # #                 if not geo_location or geo_location.lower() in skip_words:
# # #                     continue
                
# # #                 state = map_state(geo_location)
                
# # #                 # Process each column
# # #                 for m in col_meta:
# # #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# # #                     if payin is None or payin == 0:
# # #                         continue
                    
# # #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# # #                     records.append({
# # #                         "State": state,
# # #                         "Geo Location": geo_location,
# # #                         "Original Segment": m["segment"],
# # #                         "Mapped Segment": segment_final,
# # #                         "LOB": lob_final,
# # #                         "Status": "STP",
# # #                         "Payin": f"{payin:.2f}%",
# # #                         "Payin Category": get_payin_category(payin),
# # #                         "Calculated Payout": f"{payout:.2f}%",
# # #                         "Formula Used": formula,
# # #                         "Rule Explanation": explanation,
# # #                     })
# # #                     processed_count += 1
            
# # #             print(f"[CV_SATP] Extracted {len(records)} records from {processed_count} data points")
# # #             return records
            
# # #         except Exception as e:
# # #             print(f"[CV_SATP] Error: {e}")
# # #             traceback.print_exc()
# # #             return []


# # # # ===============================================================================
# # # # PATTERN DISPATCHER
# # # # ===============================================================================

# # # class CVPatternDispatcher:
# # #     """Route to correct CV processor."""
    
# # #     PATTERN_PROCESSORS = {
# # #         "cv_comp": CVCompProcessor,
# # #         "cv_satp": CVSATPProcessor,
# # #     }
    
# # #     @staticmethod
# # #     def process_sheet(content: bytes, sheet_name: str,
# # #                       override_enabled: bool = False,
# # #                       override_lob: str = None,
# # #                       override_segment: str = None) -> List[Dict]:
# # #         """Detect pattern and route to processor."""
# # #         df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
# # #         pattern = CVPatternDetector.detect_pattern(df_raw)
        
# # #         print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
# # #         processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
# # #         return processor_class.process(
# # #             content, sheet_name,
# # #             override_enabled, override_lob, override_segment
# # #         )


# # # # ===============================================================================
# # # # API ENDPOINTS
# # # # ===============================================================================

# # # @app.get("/")
# # # async def root():
# # #     return {
# # #         "message": "Carrying Vehicles Payout Processor API",
# # #         "version": "1.0.0",
# # #         "formula": "Tiered deduction based on payin ranges (independent of policy type)",
# # #         "supported_lobs": ["CV"],
# # #         "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
# # #         "supported_patterns": [
# # #             "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
# # #             "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)"
# # #         ],
# # #         "formula_tiers": [
# # #             "Payin ≤ 20%: -2%",
# # #             "Payin 21-30%: -3%",
# # #             "Payin 31-50%: -4%",
# # #             "Payin > 50%: -5%"
# # #         ]
# # #     }


# # # @app.post("/upload")
# # # async def upload_file(file: UploadFile = File(...)):
# # #     """Upload Excel file."""
# # #     try:
# # #         if not file.filename.endswith((".xlsx", ".xls")):
# # #             raise HTTPException(status_code=400, detail="Only Excel files supported")
        
# # #         content = await file.read()
# # #         xls = pd.ExcelFile(io.BytesIO(content))
# # #         sheets = xls.sheet_names
        
# # #         file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
# # #         uploaded_files[file_id] = {
# # #             "content": content,
# # #             "filename": file.filename,
# # #             "sheets": sheets,
# # #         }
        
# # #         return {
# # #             "file_id": file_id,
# # #             "filename": file.filename,
# # #             "sheets": sheets,
# # #             "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
# # #         }
        
# # #     except Exception as e:
# # #         raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


# # # @app.post("/process")
# # # async def process_sheet(
# # #     file_id: str,
# # #     sheet_name: str,
# # #     override_enabled: bool = False,
# # #     override_lob: Optional[str] = None,
# # #     override_segment: Optional[str] = None,
# # # ):
# # #     """Process worksheet."""
# # #     try:
# # #         if file_id not in uploaded_files:
# # #             raise HTTPException(status_code=404, detail="File not found")
        
# # #         file_data = uploaded_files[file_id]
        
# # #         if sheet_name not in file_data["sheets"]:
# # #             raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
# # #         records = CVPatternDispatcher.process_sheet(
# # #             file_data["content"], 
# # #             sheet_name,
# # #             override_enabled, 
# # #             override_lob, 
# # #             override_segment,
# # #         )
        
# # #         if not records:
# # #             return {
# # #                 "success": False,
# # #                 "message": "No records extracted. Check sheet structure.",
# # #                 "records": [],
# # #                 "count": 0,
# # #             }
        
# # #         # Summary stats
# # #         states = {}
# # #         payins = []
# # #         payouts = []
        
# # #         for r in records:
# # #             state = r.get("State", "UNKNOWN")
# # #             states[state] = states.get(state, 0) + 1
            
# # #             try:
# # #                 payin_val = float(r.get("Payin", "0%").replace("%", ""))
# # #                 payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
# # #                 payins.append(payin_val)
# # #                 payouts.append(payout_val)
# # #             except Exception:
# # #                 pass
        
# # #         avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
# # #         avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
# # #         return {
# # #             "success": True,
# # #             "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
# # #             "records": records,
# # #             "count": len(records),
# # #             "summary": {
# # #                 "total_records": len(records),
# # #                 "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
# # #                 "average_payin": avg_payin,
# # #                 "average_payout": avg_payout,
# # #             },
# # #         }
        
# # #     except Exception as e:
# # #         traceback.print_exc()
# # #         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


# # # @app.post("/export")
# # # async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
# # #     """Export to Excel."""
# # #     try:
# # #         if not records:
# # #             raise HTTPException(status_code=400, detail="No records to export")
        
# # #         df = pd.DataFrame(records)
        
# # #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # #         filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
# # #         out_path = os.path.join(tempfile.gettempdir(), filename)
        
# # #         with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
# # #             df.to_excel(writer, index=False, sheet_name="Processed Data")
            
# # #             worksheet = writer.sheets["Processed Data"]
# # #             for idx, col in enumerate(df.columns):
# # #                 max_length = max(
# # #                     df[col].astype(str).apply(len).max(),
# # #                     len(str(col))
# # #                 )
# # #                 worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
# # #         return FileResponse(
# # #             path=out_path,
# # #             filename=filename,
# # #             media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
# # #         )
        
# # #     except Exception as e:
# # #         raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


# # # @app.get("/health")
# # # async def health_check():
# # #     """Health check."""
# # #     return {
# # #         "status": "healthy",
# # #         "timestamp": datetime.now().isoformat(),
# # #         "uploaded_files": len(uploaded_files)
# # #     }


# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     print("\n" + "=" * 70)
# # #     print("Carrying Vehicles Payout Processor API - v1.0.0")
# # #     print("Patterns: CV COMP + CV SATP")
# # #     print("Formula: Independent of policy type, tiered deductions")
# # #     print("=" * 70 + "\n")
# # #     uvicorn.run(app, host="0.0.0.0", port=8000)

# # from fastapi import FastAPI, File, UploadFile, HTTPException
# # from fastapi.middleware.cors import CORSMiddleware
# # from fastapi.responses import FileResponse, JSONResponse
# # import pandas as pd
# # import io
# # import os
# # from typing import List, Dict, Tuple, Optional
# # from datetime import datetime
# # import traceback
# # import tempfile

# # app = FastAPI(title="Carrying Vehicles Payout Processor API")

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # ===============================================================================
# # # FORMULA DATA
# # # ===============================================================================
# # FORMULA_DATA = [
# #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
# #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
# #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
# #     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# # ]

# # # ===============================================================================
# # # STATE MAPPING
# # # ===============================================================================
# # STATE_MAPPING = {
# #     "ANDHRA PRADESH": "ANDHRA PRADESH",
# #     "KRISHNA": "ANDHRA PRADESH",
# #     "VIJAYWADA": "ANDHRA PRADESH",
# #     "VIJAYAWADA": "ANDHRA PRADESH",
# #     "VISAKHAPATNAM": "ANDHRA PRADESH",
    
# #     "KARNATAKA": "KARNATAKA",
# #     "BANGALORE": "KARNATAKA",
# #     "BENGALURU": "KARNATAKA",
    
# #     "KERALA": "KERALA",
# #     "ERNAKULAM": "KERALA",
# #     "COCHIN": "KERALA",
    
# #     "TAMIL NADU": "TAMIL NADU",
# #     "CHENNAI": "TAMIL NADU",
# #     "PONDICHERRY": "TAMIL NADU",
    
# #     "TELANGANA": "TELANGANA",
# #     "HYDERABAD": "TELANGANA",
    
# #     "MAHARASHTRA": "MAHARASHTRA",
# #     "MUMBAI": "MAHARASHTRA",
# #     "PUNE": "MAHARASHTRA",
# #     "NAGPUR": "MAHARASHTRA",
    
# #     "MADHYA PRADESH": "MADHYA PRADESH",
# #     "BHOPAL": "MADHYA PRADESH",
# #     "GWALIOR": "MADHYA PRADESH",
# #     "JABALPUR": "MADHYA PRADESH",
    
# #     "CHANDIGARH": "CHANDIGARH",
# #     "DELHI": "DELHI",
# #     "NCR": "DELHI",
# #     "GOA": "GOA",
    
# #     "HIMACHAL PRADESH": "HIMACHAL PRADESH",
# #     "BILASPUR": "HIMACHAL PRADESH",
# #     "MANDI": "HIMACHAL PRADESH",
# #     "SOLAN": "HIMACHAL PRADESH",
# #     "SHIMLA": "HIMACHAL PRADESH",
# #     "MANALI": "HIMACHAL PRADESH",
# # }

# # uploaded_files = {}

# # # ===============================================================================
# # # HELPER FUNCTIONS
# # # ===============================================================================

# # def cell_to_str(val) -> str:
# #     """Safely convert ANY cell value to string."""
# #     if val is None:
# #         return ""
# #     try:
# #         if pd.isna(val):
# #             return ""
# #     except (TypeError, ValueError):
# #         pass
# #     return str(val).strip()


# # def safe_float(value) -> Optional[float]:
# #     """Safely convert value to float, handling percentages."""
# #     if value is None:
# #         return None
# #     try:
# #         if pd.isna(value):
# #             return None
# #     except (TypeError, ValueError):
# #         pass
    
# #     s = str(value).strip().upper().replace("%", "")
# #     if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
# #         return None
    
# #     try:
# #         num = float(s)
# #         if num < 0:
# #             return None
# #         return num * 100 if 0 < num < 1 else num
# #     except Exception:
# #         return None


# # def map_state(location: str) -> str:
# #     """Map location to state."""
# #     location_upper = location.upper()
    
# #     for key, val in STATE_MAPPING.items():
# #         if key.upper() in location_upper:
# #             return val
    
# #     return location


# # def get_payin_category(payin: float) -> str:
# #     """Get payin category."""
# #     if payin <= 20:
# #         return "Payin Below 20%"
# #     elif payin <= 30:
# #         return "Payin 21% to 30%"
# #     elif payin <= 50:
# #         return "Payin 31% to 50%"
# #     else:
# #         return "Payin Above 50%"


# # def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
# #     """
# #     Calculate payout for CV based on payin ranges.
# #     CV is independent of policy type - uses tiered deductions.
# #     """
# #     if payin is None or payin == 0:
# #         return 0, "0% (No Payin)", "Payin is 0"
    
# #     payin_cat = get_payin_category(payin)
    
# #     if payin <= 20:
# #         deduction = 2
# #     elif payin <= 30:
# #         deduction = 3
# #     elif payin <= 50:
# #         deduction = 4
# #     else:
# #         deduction = 5
    
# #     payout = round(payin - deduction, 2)
# #     formula = f"-{deduction}%"
# #     explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
# #     return payout, formula, explanation


# # # ===============================================================================
# # # PATTERN DETECTION
# # # ===============================================================================

# # class CVPatternDetector:
# #     """Detect CV pattern type."""
    
# #     @staticmethod
# #     def detect_pattern(df: pd.DataFrame) -> str:
# #         """
# #         Detect pattern:
# #         - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
# #         - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
# #         """
# #         sample_text = ""
# #         for i in range(min(10, df.shape[0])):
# #             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# #             sample_text += row_text + " "
        
# #         # Check for CV SATP
# #         if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
# #            ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
# #             return "cv_satp"
        
# #         # Check for CV COMP
# #         if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
# #            ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
# #             return "cv_comp"
        
# #         # Default
# #         return "cv_comp"


# # # ===============================================================================
# # # CV COMP PROCESSOR
# # # ===============================================================================

# # class CVCompProcessor:
# #     """Process CV COMP sheets."""
    
# #     @staticmethod
# #     def process(content: bytes, sheet_name: str,
# #                 override_enabled: bool = False,
# #                 override_lob: str = None,
# #                 override_segment: str = None) -> List[Dict]:
# #         """
# #         Process CV COMP pattern:
# #         Row 1: Title (JAN 2025 CV)
# #         Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
# #         Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
# #         Row 5+: Data rows
# #         """
# #         records = []
        
# #         try:
# #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# #             print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
# #             print(f"[CV_COMP] Sheet shape: {df.shape}")
            
# #             # Find header row with "Geo Segments"
# #             header_row = None
# #             for i in range(min(10, df.shape[0])):
# #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# #                 if "GEO SEGMENT" in row_text:
# #                     header_row = i
# #                     break
            
# #             if header_row is None:
# #                 print("[CV_COMP] Header row not found")
# #                 return records
            
# #             print(f"[CV_COMP] Found header row at index: {header_row}")
            
# #             # Next row might have age bands (New, >1-5 Years, etc.)
# #             age_row = header_row + 1
            
# #             # Data starts after age row
# #             data_start = age_row + 1
# #             for i in range(data_start, df.shape[0]):
# #                 if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
# #                     data_start = i
# #                     break
            
# #             print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
# #             # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
# #             col_meta = []
# #             for col_idx in range(2, df.shape[1]):
# #                 tonnage = cell_to_str(df.iloc[header_row, col_idx])
# #                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
# #                 if not tonnage and not age_band:
# #                     continue
                
# #                 # Build segment description
# #                 segment_desc = ""
# #                 if tonnage:
# #                     segment_desc = tonnage
# #                 if age_band:
# #                     segment_desc += f" ({age_band})" if segment_desc else age_band
                
# #                 col_meta.append({
# #                     "col_idx": col_idx,
# #                     "tonnage": tonnage,
# #                     "age_band": age_band,
# #                     "segment_desc": segment_desc,
# #                 })
            
# #             if not col_meta:
# #                 print("[CV_COMP] No data columns found")
# #                 return records
            
# #             print(f"[CV_COMP] Found {len(col_meta)} columns")
# #             for m in col_meta[:5]:
# #                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
# #             # Process data rows
# #             lob_final = override_lob if override_enabled and override_lob else "CV"
# #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# #             for row_idx in range(data_start, df.shape[0]):
# #                 geo_segments = cell_to_str(df.iloc[row_idx, 0])
# #                 geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
# #                 if not geo_segments and not geo_segment_cv:
# #                     continue
                
# #                 if geo_segments.lower() in skip_words:
# #                     continue
                
# #                 # Combine both geo columns
# #                 combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
# #                 # Extract state
# #                 state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
# #                 # Process each column
# #                 for m in col_meta:
# #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# #                     if payin is None or payin == 0:
# #                         continue
                    
# #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# #                     records.append({
# #                         "State": state,
# #                         "Geo Location": combined_location,
# #                         "Geo Segments": geo_segments,
# #                         "Geo Segment CV": geo_segment_cv,
# #                         "Original Segment": m["segment_desc"],
# #                         "Tonnage": m["tonnage"],
# #                         "Age Band": m["age_band"],
# #                         "Mapped Segment": segment_final,
# #                         "LOB": lob_final,
# #                         "Status": "STP",
# #                         "Payin": f"{payin:.2f}%",
# #                         "Payin Category": get_payin_category(payin),
# #                         "Calculated Payout": f"{payout:.2f}%",
# #                         "Formula Used": formula,
# #                         "Rule Explanation": explanation,
# #                     })
            
# #             print(f"[CV_COMP] Extracted {len(records)} records")
# #             return records
            
# #         except Exception as e:
# #             print(f"[CV_COMP] Error: {e}")
# #             traceback.print_exc()
# #             return []


# # # ===============================================================================
# # # CV SATP PROCESSOR
# # # ===============================================================================

# # class CVSATPProcessor:
# #     """Process CV SATP sheets."""
    
# #     @staticmethod
# #     def process(content: bytes, sheet_name: str,
# #                 override_enabled: bool = False,
# #                 override_lob: str = None,
# #                 override_segment: str = None) -> List[Dict]:
# #         """
# #         Process CV SATP pattern:
# #         Row 1: Title (JAN 2025 PAYOUT_CV SATP)
# #         Row 2: Segment | Upto 2.5 Ton GCV 4W GCV 3W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
# #         Row 3: Geo Location - New | (empty or merged)
# #         Row 5+: Data rows
# #         """
# #         records = []
        
# #         try:
# #             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
# #             print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
# #             print(f"[CV_SATP] Sheet shape: {df.shape}")
            
# #             # Find the "Segment" row (contains tonnage categories)
# #             segment_row = None
# #             geo_row = None
            
# #             for i in range(min(10, df.shape[0])):
# #                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
# #                 first_cell = cell_to_str(df.iloc[i, 0]).upper()
                
# #                 # Row with "SEGMENT" (or typo "SEGEMENT") in first column
# #                 # Check if other columns have tonnage data
# #                 if ("SEGMENT" in first_cell or "SEGEMENT" in first_cell):
# #                     # Check if this row or next row has tonnage info
# #                     has_tonnage = False
# #                     for j in range(1, min(6, df.shape[1])):
# #                         cell_val = cell_to_str(df.iloc[i, j]).upper()
# #                         if cell_val and ("TON" in cell_val or "GCV" in cell_val or "PCV" in cell_val or "T" in cell_val):
# #                             has_tonnage = True
# #                             break
                    
# #                     if has_tonnage:
# #                         segment_row = i
# #                         print(f"[CV_SATP] Found segment row at index: {i}")
                
# #                 # Row with "GEO LOCATION" in first column
# #                 if "GEO LOCATION" in first_cell:
# #                     geo_row = i
# #                     print(f"[CV_SATP] Found geo row at index: {i}")
            
# #             if segment_row is None:
# #                 print("[CV_SATP] Segment row not found")
# #                 print("[CV_SATP] First 10 rows:")
# #                 for i in range(min(10, df.shape[0])):
# #                     print(f"  Row {i} Col 0: '{cell_to_str(df.iloc[i, 0])}'")
# #                     if df.shape[1] > 1:
# #                         print(f"    Col 1: '{cell_to_str(df.iloc[i, 1])}'")
# #                 return records
            
# #             print(f"[CV_SATP] Using segment row: {segment_row}")
            
# #             # Build column metadata from segment row AND geo row (they might be split)
# #             # Row 1: Segement | Upto 2.5 Ton | >2.5~3.5 T | >3.5~7.5 T | PCV 3W
# #             # Row 2: Geo Location - New | GCV 4W | (empty) | (empty) | Autorickshaw
# #             # Combined: Upto 2.5 Ton GCV 4W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
            
# #             col_meta = []
# #             for col_idx in range(1, df.shape[1]):
# #                 segment_part1 = cell_to_str(df.iloc[segment_row, col_idx])
# #                 segment_part2 = ""
                
# #                 # If we have a geo_row, try to get second part of header
# #                 if geo_row is not None and geo_row > segment_row:
# #                     segment_part2 = cell_to_str(df.iloc[geo_row, col_idx])
                
# #                 # Combine both parts
# #                 if segment_part1 and segment_part2:
# #                     combined_segment = f"{segment_part1} {segment_part2}".strip()
# #                 elif segment_part1:
# #                     combined_segment = segment_part1.strip()
# #                 elif segment_part2:
# #                     combined_segment = segment_part2.strip()
# #                 else:
# #                     continue
                
# #                 if not combined_segment:
# #                     continue
                
# #                 col_meta.append({
# #                     "col_idx": col_idx,
# #                     "segment": combined_segment,
# #                 })
            
# #             if not col_meta:
# #                 print("[CV_SATP] No data columns found")
# #                 print(f"[CV_SATP] Segment row content:")
# #                 for col_idx in range(df.shape[1]):
# #                     print(f"  Col {col_idx}: '{cell_to_str(df.iloc[segment_row, col_idx])}'")
# #                 if geo_row is not None:
# #                     print(f"[CV_SATP] Geo row content:")
# #                     for col_idx in range(df.shape[1]):
# #                         print(f"  Col {col_idx}: '{cell_to_str(df.iloc[geo_row, col_idx])}'")
# #                 return records
            
# #             # Data starts after geo_row (or segment_row + 1 if no geo_row found)
# #             if geo_row is not None:
# #                 data_start = geo_row + 1
# #             else:
# #                 data_start = segment_row + 1
            
# #             # Skip empty rows
# #             for i in range(data_start, df.shape[0]):
# #                 if cell_to_str(df.iloc[i, 0]):
# #                     data_start = i
# #                     break
            
# #             print(f"[CV_SATP] Data starts at row: {data_start}")
            
# #             print(f"[CV_SATP] Found {len(col_meta)} columns:")
# #             for m in col_meta:
# #                 print(f"  - Col {m['col_idx']}: '{m['segment']}'")
            
# #             # Process data rows
# #             lob_final = override_lob if override_enabled and override_lob else "CV"
# #             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
# #             skip_words = {"total", "grand total", "average", "sum", ""}
            
# #             processed_count = 0
# #             for row_idx in range(data_start, df.shape[0]):
# #                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
# #                 if not geo_location or geo_location.lower() in skip_words:
# #                     continue
                
# #                 state = map_state(geo_location)
                
# #                 # Process each column
# #                 for m in col_meta:
# #                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
# #                     if payin is None or payin == 0:
# #                         continue
                    
# #                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
# #                     records.append({
# #                         "State": state,
# #                         "Geo Location": geo_location,
# #                         "Original Segment": m["segment"],
# #                         "Mapped Segment": segment_final,
# #                         "LOB": lob_final,
# #                         "Status": "STP",
# #                         "Payin": f"{payin:.2f}%",
# #                         "Payin Category": get_payin_category(payin),
# #                         "Calculated Payout": f"{payout:.2f}%",
# #                         "Formula Used": formula,
# #                         "Rule Explanation": explanation,
# #                     })
# #                     processed_count += 1
            
# #             print(f"[CV_SATP] Extracted {len(records)} records from {processed_count} data points")
# #             return records
            
# #         except Exception as e:
# #             print(f"[CV_SATP] Error: {e}")
# #             traceback.print_exc()
# #             return []


# # # ===============================================================================
# # # PATTERN DISPATCHER
# # # ===============================================================================

# # class CVPatternDispatcher:
# #     """Route to correct CV processor."""
    
# #     PATTERN_PROCESSORS = {
# #         "cv_comp": CVCompProcessor,
# #         "cv_satp": CVSATPProcessor,
# #     }
    
# #     @staticmethod
# #     def process_sheet(content: bytes, sheet_name: str,
# #                       override_enabled: bool = False,
# #                       override_lob: str = None,
# #                       override_segment: str = None) -> List[Dict]:
# #         """Detect pattern and route to processor."""
# #         df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
# #         pattern = CVPatternDetector.detect_pattern(df_raw)
        
# #         print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
# #         processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
# #         return processor_class.process(
# #             content, sheet_name,
# #             override_enabled, override_lob, override_segment
# #         )


# # # ===============================================================================
# # # API ENDPOINTS
# # # ===============================================================================

# # @app.get("/")
# # async def root():
# #     return {
# #         "message": "Carrying Vehicles Payout Processor API",
# #         "version": "1.0.0",
# #         "formula": "Tiered deduction based on payin ranges (independent of policy type)",
# #         "supported_lobs": ["CV"],
# #         "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
# #         "supported_patterns": [
# #             "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
# #             "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)"
# #         ],
# #         "formula_tiers": [
# #             "Payin ≤ 20%: -2%",
# #             "Payin 21-30%: -3%",
# #             "Payin 31-50%: -4%",
# #             "Payin > 50%: -5%"
# #         ]
# #     }


# # @app.post("/upload")
# # async def upload_file(file: UploadFile = File(...)):
# #     """Upload Excel file."""
# #     try:
# #         if not file.filename.endswith((".xlsx", ".xls")):
# #             raise HTTPException(status_code=400, detail="Only Excel files supported")
        
# #         content = await file.read()
# #         xls = pd.ExcelFile(io.BytesIO(content))
# #         sheets = xls.sheet_names
        
# #         file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
# #         uploaded_files[file_id] = {
# #             "content": content,
# #             "filename": file.filename,
# #             "sheets": sheets,
# #         }
        
# #         return {
# #             "file_id": file_id,
# #             "filename": file.filename,
# #             "sheets": sheets,
# #             "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
# #         }
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


# # @app.post("/process")
# # async def process_sheet(
# #     file_id: str,
# #     sheet_name: str,
# #     override_enabled: bool = False,
# #     override_lob: Optional[str] = None,
# #     override_segment: Optional[str] = None,
# # ):
# #     """Process worksheet."""
# #     try:
# #         if file_id not in uploaded_files:
# #             raise HTTPException(status_code=404, detail="File not found")
        
# #         file_data = uploaded_files[file_id]
        
# #         if sheet_name not in file_data["sheets"]:
# #             raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
# #         records = CVPatternDispatcher.process_sheet(
# #             file_data["content"], 
# #             sheet_name,
# #             override_enabled, 
# #             override_lob, 
# #             override_segment,
# #         )
        
# #         if not records:
# #             return {
# #                 "success": False,
# #                 "message": "No records extracted. Check sheet structure.",
# #                 "records": [],
# #                 "count": 0,
# #             }
        
# #         # Summary stats
# #         states = {}
# #         payins = []
# #         payouts = []
        
# #         for r in records:
# #             state = r.get("State", "UNKNOWN")
# #             states[state] = states.get(state, 0) + 1
            
# #             try:
# #                 payin_val = float(r.get("Payin", "0%").replace("%", ""))
# #                 payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
# #                 payins.append(payin_val)
# #                 payouts.append(payout_val)
# #             except Exception:
# #                 pass
        
# #         avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
# #         avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
# #         return {
# #             "success": True,
# #             "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
# #             "records": records,
# #             "count": len(records),
# #             "summary": {
# #                 "total_records": len(records),
# #                 "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
# #                 "average_payin": avg_payin,
# #                 "average_payout": avg_payout,
# #             },
# #         }
        
# #     except Exception as e:
# #         traceback.print_exc()
# #         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


# # @app.post("/export")
# # async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
# #     """Export to Excel."""
# #     try:
# #         if not records:
# #             raise HTTPException(status_code=400, detail="No records to export")
        
# #         df = pd.DataFrame(records)
        
# #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# #         filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
# #         out_path = os.path.join(tempfile.gettempdir(), filename)
        
# #         with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
# #             df.to_excel(writer, index=False, sheet_name="Processed Data")
            
# #             worksheet = writer.sheets["Processed Data"]
# #             for idx, col in enumerate(df.columns):
# #                 max_length = max(
# #                     df[col].astype(str).apply(len).max(),
# #                     len(str(col))
# #                 )
# #                 worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
# #         return FileResponse(
# #             path=out_path,
# #             filename=filename,
# #             media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
# #         )
        
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


# # @app.get("/health")
# # async def health_check():
# #     """Health check."""
# #     return {
# #         "status": "healthy",
# #         "timestamp": datetime.now().isoformat(),
# #         "uploaded_files": len(uploaded_files)
# #     }


# # if __name__ == "__main__":
# #     import uvicorn
# #     print("\n" + "=" * 70)
# #     print("Carrying Vehicles Payout Processor API - v1.0.0")
# #     print("Patterns: CV COMP + CV SATP")
# #     print("Formula: Independent of policy type, tiered deductions")
# #     print("=" * 70 + "\n")
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse, JSONResponse
# import pandas as pd
# import io
# import os
# from typing import List, Dict, Tuple, Optional
# from datetime import datetime
# import traceback
# import tempfile

# app = FastAPI(title="Carrying Vehicles Payout Processor API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ===============================================================================
# # FORMULA DATA
# # ===============================================================================
# FORMULA_DATA = [
#     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
#     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
#     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
#     {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
# ]

# # ===============================================================================
# # STATE MAPPING
# # ===============================================================================
# STATE_MAPPING = {
#     "ANDHRA PRADESH": "ANDHRA PRADESH",
#     "KRISHNA": "ANDHRA PRADESH",
#     "VIJAYWADA": "ANDHRA PRADESH",
#     "VIJAYAWADA": "ANDHRA PRADESH",
#     "VISAKHAPATNAM": "ANDHRA PRADESH",
    
#     "KARNATAKA": "KARNATAKA",
#     "BANGALORE": "KARNATAKA",
#     "BENGALURU": "KARNATAKA",
    
#     "KERALA": "KERALA",
#     "ERNAKULAM": "KERALA",
#     "COCHIN": "KERALA",
    
#     "TAMIL NADU": "TAMIL NADU",
#     "CHENNAI": "TAMIL NADU",
#     "PONDICHERRY": "TAMIL NADU",
    
#     "TELANGANA": "TELANGANA",
#     "HYDERABAD": "TELANGANA",
    
#     "MAHARASHTRA": "MAHARASHTRA",
#     "MUMBAI": "MAHARASHTRA",
#     "PUNE": "MAHARASHTRA",
#     "NAGPUR": "MAHARASHTRA",
    
#     "MADHYA PRADESH": "MADHYA PRADESH",
#     "BHOPAL": "MADHYA PRADESH",
#     "GWALIOR": "MADHYA PRADESH",
#     "JABALPUR": "MADHYA PRADESH",
    
#     "CHANDIGARH": "CHANDIGARH",
#     "DELHI": "DELHI",
#     "NCR": "DELHI",
#     "GOA": "GOA",
    
#     "HIMACHAL PRADESH": "HIMACHAL PRADESH",
#     "BILASPUR": "HIMACHAL PRADESH",
#     "MANDI": "HIMACHAL PRADESH",
#     "SOLAN": "HIMACHAL PRADESH",
#     "SHIMLA": "HIMACHAL PRADESH",
#     "MANALI": "HIMACHAL PRADESH",
# }

# uploaded_files = {}

# # ===============================================================================
# # HELPER FUNCTIONS
# # ===============================================================================

# def cell_to_str(val) -> str:
#     """Safely convert ANY cell value to string."""
#     if val is None:
#         return ""
#     try:
#         if pd.isna(val):
#             return ""
#     except (TypeError, ValueError):
#         pass
#     return str(val).strip()


# def safe_float(value) -> Optional[float]:
#     """Safely convert value to float, handling percentages."""
#     if value is None:
#         return None
#     try:
#         if pd.isna(value):
#             return None
#     except (TypeError, ValueError):
#         pass
    
#     s = str(value).strip().upper().replace("%", "")
#     if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
#         return None
    
#     try:
#         num = float(s)
#         if num < 0:
#             return None
#         return num * 100 if 0 < num < 1 else num
#     except Exception:
#         return None


# def map_state(location: str) -> str:
#     """Map location to state."""
#     location_upper = location.upper()
    
#     for key, val in STATE_MAPPING.items():
#         if key.upper() in location_upper:
#             return val
    
#     return location


# def get_payin_category(payin: float) -> str:
#     """Get payin category."""
#     if payin <= 20:
#         return "Payin Below 20%"
#     elif payin <= 30:
#         return "Payin 21% to 30%"
#     elif payin <= 50:
#         return "Payin 31% to 50%"
#     else:
#         return "Payin Above 50%"


# def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
#     """
#     Calculate payout for CV based on payin ranges.
#     CV is independent of policy type - uses tiered deductions.
#     """
#     if payin is None or payin == 0:
#         return 0, "0% (No Payin)", "Payin is 0"
    
#     payin_cat = get_payin_category(payin)
    
#     if payin <= 20:
#         deduction = 2
#     elif payin <= 30:
#         deduction = 3
#     elif payin <= 50:
#         deduction = 4
#     else:
#         deduction = 5
    
#     payout = round(payin - deduction, 2)
#     formula = f"-{deduction}%"
#     explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
#     return payout, formula, explanation


# # ===============================================================================
# # PATTERN DETECTION
# # ===============================================================================

# class CVPatternDetector:
#     """Detect CV pattern type."""
    
#     @staticmethod
#     def detect_pattern(df: pd.DataFrame) -> str:
#         """
#         Detect pattern:
#         - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
#         - 'cv_comp_tonnage_age': CV COMP with tonnage row + age row (0-2.5T, 2.5-3.5T, etc.)
#         - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
#         """
#         sample_text = ""
#         for i in range(min(10, df.shape[0])):
#             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
#             sample_text += row_text + " "
        
#         # Check for CV COMP with tonnage-age pattern (0-2.5T, 2.5-3.5T structure)
#         has_tonnage_range = False
#         has_age_bands = False
        
#         for i in range(min(10, df.shape[0])):
#             row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
#             # Look for tonnage ranges like "0 - 2.5T" or "2.5 - 3.5T"
#             if ("2.5T" in row_text or "3.5T" in row_text or "7.5T" in row_text) and "-" in row_text:
#                 has_tonnage_range = True
#             # Look for age bands
#             if ("NEW" in row_text and "YEARS" in row_text) or (">1 - 5 YEARS" in row_text or ">5 - 10" in row_text):
#                 has_age_bands = True
        
#         if has_tonnage_range and has_age_bands and "GEO LOCATION" in sample_text:
#             return "cv_comp_tonnage_age"
        
#         # Check for CV SATP
#         if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
#            ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
#             return "cv_satp"
        
#         # Check for CV COMP (original pattern)
#         if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
#            ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
#             return "cv_comp"
        
#         # Default
#         return "cv_comp"


# # ===============================================================================
# # CV COMP PROCESSOR
# # ===============================================================================

# class CVCompProcessor:
#     """Process CV COMP sheets."""
    
#     @staticmethod
#     def process(content: bytes, sheet_name: str,
#                 override_enabled: bool = False,
#                 override_lob: str = None,
#                 override_segment: str = None) -> List[Dict]:
#         """
#         Process CV COMP pattern:
#         Row 1: Title (JAN 2025 CV)
#         Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
#         Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
#         Row 5+: Data rows
#         """
#         records = []
        
#         try:
#             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
#             print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
#             print(f"[CV_COMP] Sheet shape: {df.shape}")
            
#             # Find header row with "Geo Segments"
#             header_row = None
#             for i in range(min(10, df.shape[0])):
#                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
#                 if "GEO SEGMENT" in row_text:
#                     header_row = i
#                     break
            
#             if header_row is None:
#                 print("[CV_COMP] Header row not found")
#                 return records
            
#             print(f"[CV_COMP] Found header row at index: {header_row}")
            
#             # Next row might have age bands (New, >1-5 Years, etc.)
#             age_row = header_row + 1
            
#             # Data starts after age row
#             data_start = age_row + 1
#             for i in range(data_start, df.shape[0]):
#                 if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
#                     data_start = i
#                     break
            
#             print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
#             # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
#             col_meta = []
#             for col_idx in range(2, df.shape[1]):
#                 tonnage = cell_to_str(df.iloc[header_row, col_idx])
#                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
#                 if not tonnage and not age_band:
#                     continue
                
#                 # Build segment description
#                 segment_desc = ""
#                 if tonnage:
#                     segment_desc = tonnage
#                 if age_band:
#                     segment_desc += f" ({age_band})" if segment_desc else age_band
                
#                 col_meta.append({
#                     "col_idx": col_idx,
#                     "tonnage": tonnage,
#                     "age_band": age_band,
#                     "segment_desc": segment_desc,
#                 })
            
#             if not col_meta:
#                 print("[CV_COMP] No data columns found")
#                 return records
            
#             print(f"[CV_COMP] Found {len(col_meta)} columns")
#             for m in col_meta[:5]:
#                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
#             # Process data rows
#             lob_final = override_lob if override_enabled and override_lob else "CV"
#             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
#             skip_words = {"total", "grand total", "average", "sum", ""}
            
#             for row_idx in range(data_start, df.shape[0]):
#                 geo_segments = cell_to_str(df.iloc[row_idx, 0])
#                 geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
#                 if not geo_segments and not geo_segment_cv:
#                     continue
                
#                 if geo_segments.lower() in skip_words:
#                     continue
                
#                 # Combine both geo columns
#                 combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
#                 # Extract state
#                 state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
#                 # Process each column
#                 for m in col_meta:
#                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
#                     if payin is None or payin == 0:
#                         continue
                    
#                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
#                     records.append({
#                         "State": state,
#                         "Geo Location": combined_location,
#                         "Geo Segments": geo_segments,
#                         "Geo Segment CV": geo_segment_cv,
#                         "Original Segment": m["segment_desc"],
#                         "Tonnage": m["tonnage"],
#                         "Age Band": m["age_band"],
#                         "Mapped Segment": segment_final,
#                         "LOB": lob_final,
#                         "Status": "STP",
#                         "Payin": f"{payin:.2f}%",
#                         "Payin Category": get_payin_category(payin),
#                         "Calculated Payout": f"{payout:.2f}%",
#                         "Formula Used": formula,
#                         "Rule Explanation": explanation,
#                     })
            
#             print(f"[CV_COMP] Extracted {len(records)} records")
#             return records
            
#         except Exception as e:
#             print(f"[CV_COMP] Error: {e}")
#             traceback.print_exc()
#             return []


# # ===============================================================================
# # CV COMP TONNAGE-AGE PROCESSOR
# # ===============================================================================

# class CVCompTonnageAgeProcessor:
#     """Process CV COMP sheets with tonnage ranges and age bands."""
    
#     @staticmethod
#     def process(content: bytes, sheet_name: str,
#                 override_enabled: bool = False,
#                 override_lob: str = None,
#                 override_segment: str = None) -> List[Dict]:
#         """
#         Process CV COMP with tonnage-age pattern:
#         Row 2: 0 - 2.5T | 2.5 - 3.5T | 3.5 - 7.5T
#         Row 3: Geo Location - New | New | >1 - 5 Years | >5 - 10+ Years | New | >1 - 5 Years | ...
#         Row 5+: Data rows
#         """
#         records = []
        
#         try:
#             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
#             print(f"\n[CV_COMP_TONNAGE_AGE] Processing sheet: {sheet_name}")
#             print(f"[CV_COMP_TONNAGE_AGE] Sheet shape: {df.shape}")
            
#             # Find tonnage row (0 - 2.5T, 2.5 - 3.5T, etc.)
#             tonnage_row = None
#             for i in range(min(10, df.shape[0])):
#                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
#                 if ("2.5T" in row_text or "3.5T" in row_text or "7.5T" in row_text) and "-" in row_text:
#                     tonnage_row = i
#                     break
            
#             if tonnage_row is None:
#                 print("[CV_COMP_TONNAGE_AGE] Tonnage row not found")
#                 return records
            
#             print(f"[CV_COMP_TONNAGE_AGE] Found tonnage row at index: {tonnage_row}")
            
#             # Age band row is next
#             age_row = tonnage_row + 1
            
#             # Find data start (look for "Geo Location - New" or first location)
#             data_start = age_row + 1
#             for i in range(data_start, df.shape[0]):
#                 if cell_to_str(df.iloc[i, 0]):
#                     data_start = i
#                     break
            
#             print(f"[CV_COMP_TONNAGE_AGE] Age row: {age_row}, Data starts: {data_start}")
            
#             # Build column metadata (combine tonnage + age)
#             # Column 0 is "Geo Location - New"
#             col_meta = []
#             last_tonnage = ""
            
#             for col_idx in range(1, df.shape[1]):
#                 tonnage = cell_to_str(df.iloc[tonnage_row, col_idx])
#                 age_band = cell_to_str(df.iloc[age_row, col_idx])
                
#                 # Forward fill tonnage (for merged cells)
#                 if tonnage:
#                     last_tonnage = tonnage
                
#                 if not age_band:
#                     continue
                
#                 # Build combined segment
#                 segment_desc = f"{last_tonnage} ({age_band})" if last_tonnage else age_band
                
#                 col_meta.append({
#                     "col_idx": col_idx,
#                     "tonnage": last_tonnage,
#                     "age_band": age_band,
#                     "segment_desc": segment_desc,
#                 })
            
#             if not col_meta:
#                 print("[CV_COMP_TONNAGE_AGE] No data columns found")
#                 return records
            
#             print(f"[CV_COMP_TONNAGE_AGE] Found {len(col_meta)} columns")
#             for m in col_meta[:5]:
#                 print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
#             # Process data rows
#             lob_final = override_lob if override_enabled and override_lob else "CV"
#             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
#             skip_words = {"total", "grand total", "average", "sum", ""}
            
#             for row_idx in range(data_start, df.shape[0]):
#                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
#                 if not geo_location or geo_location.lower() in skip_words:
#                     continue
                
#                 state = map_state(geo_location)
                
#                 # Process each column
#                 for m in col_meta:
#                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
#                     if payin is None or payin == 0:
#                         continue
                    
#                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
#                     records.append({
#                         "State": state,
#                         "Geo Location": geo_location,
#                         "Original Segment": m["segment_desc"],
#                         "Tonnage": m["tonnage"],
#                         "Age Band": m["age_band"],
#                         "Mapped Segment": segment_final,
#                         "LOB": lob_final,
#                         "Status": "STP",
#                         "Payin": f"{payin:.2f}%",
#                         "Payin Category": get_payin_category(payin),
#                         "Calculated Payout": f"{payout:.2f}%",
#                         "Formula Used": formula,
#                         "Rule Explanation": explanation,
#                     })
            
#             print(f"[CV_COMP_TONNAGE_AGE] Extracted {len(records)} records")
#             return records
            
#         except Exception as e:
#             print(f"[CV_COMP_TONNAGE_AGE] Error: {e}")
#             traceback.print_exc()
#             return []


# # ===============================================================================
# # CV SATP PROCESSOR
# # ===============================================================================

# class CVSATPProcessor:
#     """Process CV SATP sheets."""
    
#     @staticmethod
#     def process(content: bytes, sheet_name: str,
#                 override_enabled: bool = False,
#                 override_lob: str = None,
#                 override_segment: str = None) -> List[Dict]:
#         """
#         Process CV SATP pattern:
#         Row 1: Title (JAN 2025 PAYOUT_CV SATP)
#         Row 2: Segment | Upto 2.5 Ton GCV 4W GCV 3W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
#         Row 3: Geo Location - New | (empty or merged)
#         Row 5+: Data rows
#         """
#         records = []
        
#         try:
#             df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
#             print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
#             print(f"[CV_SATP] Sheet shape: {df.shape}")
            
#             # Find the "Segment" row (contains tonnage categories)
#             segment_row = None
#             geo_row = None
            
#             for i in range(min(10, df.shape[0])):
#                 row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
#                 first_cell = cell_to_str(df.iloc[i, 0]).upper()
                
#                 # Row with "SEGMENT" (or typo "SEGEMENT") in first column
#                 # Check if other columns have tonnage data
#                 if ("SEGMENT" in first_cell or "SEGEMENT" in first_cell):
#                     # Check if this row or next row has tonnage info
#                     has_tonnage = False
#                     for j in range(1, min(6, df.shape[1])):
#                         cell_val = cell_to_str(df.iloc[i, j]).upper()
#                         if cell_val and ("TON" in cell_val or "GCV" in cell_val or "PCV" in cell_val or "T" in cell_val):
#                             has_tonnage = True
#                             break
                    
#                     if has_tonnage:
#                         segment_row = i
#                         print(f"[CV_SATP] Found segment row at index: {i}")
                
#                 # Row with "GEO LOCATION" in first column
#                 if "GEO LOCATION" in first_cell:
#                     geo_row = i
#                     print(f"[CV_SATP] Found geo row at index: {i}")
            
#             if segment_row is None:
#                 print("[CV_SATP] Segment row not found")
#                 print("[CV_SATP] First 10 rows:")
#                 for i in range(min(10, df.shape[0])):
#                     print(f"  Row {i} Col 0: '{cell_to_str(df.iloc[i, 0])}'")
#                     if df.shape[1] > 1:
#                         print(f"    Col 1: '{cell_to_str(df.iloc[i, 1])}'")
#                 return records
            
#             print(f"[CV_SATP] Using segment row: {segment_row}")
            
#             # Build column metadata from segment row AND geo row (they might be split)
#             # Row 1: Segement | Upto 2.5 Ton | >2.5~3.5 T | >3.5~7.5 T | PCV 3W
#             # Row 2: Geo Location - New | GCV 4W | (empty) | (empty) | Autorickshaw
#             # Combined: Upto 2.5 Ton GCV 4W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
            
#             col_meta = []
#             for col_idx in range(1, df.shape[1]):
#                 segment_part1 = cell_to_str(df.iloc[segment_row, col_idx])
#                 segment_part2 = ""
                
#                 # If we have a geo_row, try to get second part of header
#                 if geo_row is not None and geo_row > segment_row:
#                     segment_part2 = cell_to_str(df.iloc[geo_row, col_idx])
                
#                 # Combine both parts
#                 if segment_part1 and segment_part2:
#                     combined_segment = f"{segment_part1} {segment_part2}".strip()
#                 elif segment_part1:
#                     combined_segment = segment_part1.strip()
#                 elif segment_part2:
#                     combined_segment = segment_part2.strip()
#                 else:
#                     continue
                
#                 if not combined_segment:
#                     continue
                
#                 col_meta.append({
#                     "col_idx": col_idx,
#                     "segment": combined_segment,
#                 })
            
#             if not col_meta:
#                 print("[CV_SATP] No data columns found")
#                 print(f"[CV_SATP] Segment row content:")
#                 for col_idx in range(df.shape[1]):
#                     print(f"  Col {col_idx}: '{cell_to_str(df.iloc[segment_row, col_idx])}'")
#                 if geo_row is not None:
#                     print(f"[CV_SATP] Geo row content:")
#                     for col_idx in range(df.shape[1]):
#                         print(f"  Col {col_idx}: '{cell_to_str(df.iloc[geo_row, col_idx])}'")
#                 return records
            
#             # Data starts after geo_row (or segment_row + 1 if no geo_row found)
#             if geo_row is not None:
#                 data_start = geo_row + 1
#             else:
#                 data_start = segment_row + 1
            
#             # Skip empty rows
#             for i in range(data_start, df.shape[0]):
#                 if cell_to_str(df.iloc[i, 0]):
#                     data_start = i
#                     break
            
#             print(f"[CV_SATP] Data starts at row: {data_start}")
            
#             print(f"[CV_SATP] Found {len(col_meta)} columns:")
#             for m in col_meta:
#                 print(f"  - Col {m['col_idx']}: '{m['segment']}'")
            
#             # Process data rows
#             lob_final = override_lob if override_enabled and override_lob else "CV"
#             segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
#             skip_words = {"total", "grand total", "average", "sum", ""}
            
#             processed_count = 0
#             for row_idx in range(data_start, df.shape[0]):
#                 geo_location = cell_to_str(df.iloc[row_idx, 0])
                
#                 if not geo_location or geo_location.lower() in skip_words:
#                     continue
                
#                 state = map_state(geo_location)
                
#                 # Process each column
#                 for m in col_meta:
#                     payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
#                     if payin is None or payin == 0:
#                         continue
                    
#                     payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
#                     records.append({
#                         "State": state,
#                         "Geo Location": geo_location,
#                         "Original Segment": m["segment"],
#                         "Mapped Segment": segment_final,
#                         "LOB": lob_final,
#                         "Status": "STP",
#                         "Payin": f"{payin:.2f}%",
#                         "Payin Category": get_payin_category(payin),
#                         "Calculated Payout": f"{payout:.2f}%",
#                         "Formula Used": formula,
#                         "Rule Explanation": explanation,
#                     })
#                     processed_count += 1
            
#             print(f"[CV_SATP] Extracted {len(records)} records from {processed_count} data points")
#             return records
            
#         except Exception as e:
#             print(f"[CV_SATP] Error: {e}")
#             traceback.print_exc()
#             return []


# # ===============================================================================
# # PATTERN DISPATCHER
# # ===============================================================================

# class CVPatternDispatcher:
#     """Route to correct CV processor."""
    
#     PATTERN_PROCESSORS = {
#         "cv_comp": CVCompProcessor,
#         "cv_comp_tonnage_age": CVCompTonnageAgeProcessor,
#         "cv_satp": CVSATPProcessor,
#     }
    
#     @staticmethod
#     def process_sheet(content: bytes, sheet_name: str,
#                       override_enabled: bool = False,
#                       override_lob: str = None,
#                       override_segment: str = None) -> List[Dict]:
#         """Detect pattern and route to processor."""
#         df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
#         pattern = CVPatternDetector.detect_pattern(df_raw)
        
#         print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
#         processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
#         return processor_class.process(
#             content, sheet_name,
#             override_enabled, override_lob, override_segment
#         )


# # ===============================================================================
# # API ENDPOINTS
# # ===============================================================================

# @app.get("/")
# async def root():
#     return {
#         "message": "Carrying Vehicles Payout Processor API",
#         "version": "2.0.0",
#         "formula": "Tiered deduction based on payin ranges (independent of policy type)",
#         "supported_lobs": ["CV"],
#         "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
#         "supported_patterns": [
#             "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
#             "cv_comp_tonnage_age - CV COMP with tonnage ranges + age bands (0-2.5T, 2.5-3.5T, etc.)",
#             "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)"
#         ],
#         "formula_tiers": [
#             "Payin ≤ 20%: -2%",
#             "Payin 21-30%: -3%",
#             "Payin 31-50%: -4%",
#             "Payin > 50%: -5%"
#         ]
#     }


# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     """Upload Excel file."""
#     try:
#         if not file.filename.endswith((".xlsx", ".xls")):
#             raise HTTPException(status_code=400, detail="Only Excel files supported")
        
#         content = await file.read()
#         xls = pd.ExcelFile(io.BytesIO(content))
#         sheets = xls.sheet_names
        
#         file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
#         uploaded_files[file_id] = {
#             "content": content,
#             "filename": file.filename,
#             "sheets": sheets,
#         }
        
#         return {
#             "file_id": file_id,
#             "filename": file.filename,
#             "sheets": sheets,
#             "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
#         }
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


# @app.post("/process")
# async def process_sheet(
#     file_id: str,
#     sheet_name: str,
#     override_enabled: bool = False,
#     override_lob: Optional[str] = None,
#     override_segment: Optional[str] = None,
# ):
#     """Process worksheet."""
#     try:
#         if file_id not in uploaded_files:
#             raise HTTPException(status_code=404, detail="File not found")
        
#         file_data = uploaded_files[file_id]
        
#         if sheet_name not in file_data["sheets"]:
#             raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
#         records = CVPatternDispatcher.process_sheet(
#             file_data["content"], 
#             sheet_name,
#             override_enabled, 
#             override_lob, 
#             override_segment,
#         )
        
#         if not records:
#             return {
#                 "success": False,
#                 "message": "No records extracted. Check sheet structure.",
#                 "records": [],
#                 "count": 0,
#             }
        
#         # Summary stats
#         states = {}
#         payins = []
#         payouts = []
        
#         for r in records:
#             state = r.get("State", "UNKNOWN")
#             states[state] = states.get(state, 0) + 1
            
#             try:
#                 payin_val = float(r.get("Payin", "0%").replace("%", ""))
#                 payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
#                 payins.append(payin_val)
#                 payouts.append(payout_val)
#             except Exception:
#                 pass
        
#         avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
#         avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
#         return {
#             "success": True,
#             "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
#             "records": records,
#             "count": len(records),
#             "summary": {
#                 "total_records": len(records),
#                 "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
#                 "average_payin": avg_payin,
#                 "average_payout": avg_payout,
#             },
#         }
        
#     except Exception as e:
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


# @app.post("/export")
# async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
#     """Export to Excel."""
#     try:
#         if not records:
#             raise HTTPException(status_code=400, detail="No records to export")
        
#         df = pd.DataFrame(records)
        
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
#         out_path = os.path.join(tempfile.gettempdir(), filename)
        
#         with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
#             df.to_excel(writer, index=False, sheet_name="Processed Data")
            
#             worksheet = writer.sheets["Processed Data"]
#             for idx, col in enumerate(df.columns):
#                 max_length = max(
#                     df[col].astype(str).apply(len).max(),
#                     len(str(col))
#                 )
#                 worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
#         return FileResponse(
#             path=out_path,
#             filename=filename,
#             media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


# @app.get("/health")
# async def health_check():
#     """Health check."""
#     return {
#         "status": "healthy",
#         "timestamp": datetime.now().isoformat(),
#         "uploaded_files": len(uploaded_files)
#     }


# if __name__ == "__main__":
#     import uvicorn
#     print("\n" + "=" * 70)
#     print("Carrying Vehicles Payout Processor API - v2.0.0")
#     print("Patterns: CV COMP + CV COMP Tonnage-Age + CV SATP")
#     print("Formula: Independent of policy type, tiered deductions")
#     print("=" * 70 + "\n")
#     uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import pandas as pd
import io
import os
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import traceback
import tempfile

app = FastAPI(title="Carrying Vehicles Payout Processor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================================================================
# FORMULA DATA
# ===============================================================================
FORMULA_DATA = [
    {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-2%", "REMARKS": "Payin Below 20%"},
    {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-3%", "REMARKS": "Payin 21% to 30%"},
    {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-4%", "REMARKS": "Payin 31% to 50%"},
    {"LOB": "CV", "SEGMENT": "All GVW & PCV 3W, GCV 3W", "PO": "-5%", "REMARKS": "Payin Above 50%"},
]

# ===============================================================================
# STATE MAPPING
# ===============================================================================
STATE_MAPPING = {
    "ANDHRA PRADESH": "ANDHRA PRADESH",
    "KRISHNA": "ANDHRA PRADESH",
    "VIJAYWADA": "ANDHRA PRADESH",
    "VIJAYAWADA": "ANDHRA PRADESH",
    "VISAKHAPATNAM": "ANDHRA PRADESH",
    
    "KARNATAKA": "KARNATAKA",
    "BANGALORE": "KARNATAKA",
    "BENGALURU": "KARNATAKA",
    
    "KERALA": "KERALA",
    "ERNAKULAM": "KERALA",
    "COCHIN": "KERALA",
    
    "TAMIL NADU": "TAMIL NADU",
    "CHENNAI": "TAMIL NADU",
    "PONDICHERRY": "TAMIL NADU",
    
    "TELANGANA": "TELANGANA",
    "HYDERABAD": "TELANGANA",
    
    "MAHARASHTRA": "MAHARASHTRA",
    "MUMBAI": "MAHARASHTRA",
    "PUNE": "MAHARASHTRA",
    "NAGPUR": "MAHARASHTRA",
    
    "MADHYA PRADESH": "MADHYA PRADESH",
    "BHOPAL": "MADHYA PRADESH",
    "GWALIOR": "MADHYA PRADESH",
    "JABALPUR": "MADHYA PRADESH",
    
    "CHANDIGARH": "CHANDIGARH",
    "DELHI": "DELHI",
    "NCR": "DELHI",
    "GOA": "GOA",
    
    "HIMACHAL PRADESH": "HIMACHAL PRADESH",
    "BILASPUR": "HIMACHAL PRADESH",
    "MANDI": "HIMACHAL PRADESH",
    "SOLAN": "HIMACHAL PRADESH",
    "SHIMLA": "HIMACHAL PRADESH",
    "MANALI": "HIMACHAL PRADESH",
}

uploaded_files = {}

# ===============================================================================
# HELPER FUNCTIONS
# ===============================================================================

def cell_to_str(val) -> str:
    """Safely convert ANY cell value to string."""
    if val is None:
        return ""
    try:
        if pd.isna(val):
            return ""
    except (TypeError, ValueError):
        pass
    return str(val).strip()


def safe_float(value) -> Optional[float]:
    """Safely convert value to float, handling percentages."""
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    
    s = str(value).strip().upper().replace("%", "")
    if s in ["D", "NA", "", "NAN", "NONE", "DECLINE", "0.00%", "0.0%", "0%"]:
        return None
    
    try:
        num = float(s)
        if num < 0:
            return None
        return num * 100 if 0 < num < 1 else num
    except Exception:
        return None


def map_state(location: str) -> str:
    """Map location to state."""
    location_upper = location.upper()
    
    for key, val in STATE_MAPPING.items():
        if key.upper() in location_upper:
            return val
    
    return location


def get_payin_category(payin: float) -> str:
    """Get payin category."""
    if payin <= 20:
        return "Payin Below 20%"
    elif payin <= 30:
        return "Payin 21% to 30%"
    elif payin <= 50:
        return "Payin 31% to 50%"
    else:
        return "Payin Above 50%"


def calculate_payout(payin: float, lob: str = "CV", segment: str = "All GVW & PCV 3W, GCV 3W") -> Tuple[float, str, str]:
    """
    Calculate payout for CV based on payin ranges.
    CV is independent of policy type - uses tiered deductions.
    """
    if payin is None or payin == 0:
        return 0, "0% (No Payin)", "Payin is 0"
    
    payin_cat = get_payin_category(payin)
    
    if payin <= 20:
        deduction = 2
    elif payin <= 30:
        deduction = 3
    elif payin <= 50:
        deduction = 4
    else:
        deduction = 5
    
    payout = round(payin - deduction, 2)
    formula = f"-{deduction}%"
    explanation = f"Applied formula: {formula} for CV, {payin_cat}"
    
    return payout, formula, explanation


# ===============================================================================
# PATTERN DETECTION
# ===============================================================================

class CVPatternDetector:
    """Detect CV pattern type."""
    
    @staticmethod
    def detect_pattern(df: pd.DataFrame) -> str:
        """
        Detect pattern:
        - 'cv_comp': CV COMP pattern (Geo Segments | Geo Segment CV | Age bands)
        - 'cv_comp_tonnage_age': CV COMP with tonnage row + age row (0-2.5T, 2.5-3.5T, etc.)
        - 'cv_satp': CV SATP pattern (Segment | Geo Location - New | Tonnage categories)
        - 'cv_satp_geo_new_old': CV SATP with Geo New/Old + tonnage + age bands
        """
        sample_text = ""
        for i in range(min(10, df.shape[0])):
            row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
            sample_text += row_text + " "
        
        # Check for CV SATP with Geo New/Old (has both geo segment columns + tonnage + age)
        has_geo_new_old = "GEO SEGMENT NEW" in sample_text and "GEO SEGMENT OLD" in sample_text
        has_cv_satp = "CVSATP" in sample_text or "CV SATP" in sample_text
        has_tonnage_age = ("2.5 TON" in sample_text or "3.5 TON" in sample_text) and \
                          ("NEW" in sample_text and "YEARS" in sample_text)
        
        if has_geo_new_old and has_cv_satp and has_tonnage_age:
            return "cv_satp_geo_new_old"
        
        # Check for CV COMP with tonnage-age pattern (0-2.5T, 2.5-3.5T structure)
        has_tonnage_range = False
        has_age_bands = False
        
        for i in range(min(10, df.shape[0])):
            row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
            # Look for tonnage ranges like "0 - 2.5T" or "2.5 - 3.5T"
            if ("2.5T" in row_text or "3.5T" in row_text or "7.5T" in row_text) and "-" in row_text:
                has_tonnage_range = True
            # Look for age bands
            if ("NEW" in row_text and "YEARS" in row_text) or (">1 - 5 YEARS" in row_text or ">5 - 10" in row_text):
                has_age_bands = True
        
        if has_tonnage_range and has_age_bands and "GEO LOCATION" in sample_text:
            return "cv_comp_tonnage_age"
        
        # Check for CV SATP
        if ("CV SATP" in sample_text or "CV_SATP" in sample_text or "PAYOUT_CV SATP" in sample_text) and \
           ("TON" in sample_text or "GCV" in sample_text or "PCV" in sample_text):
            return "cv_satp"
        
        # Check for CV COMP (original pattern)
        if ("CV" in sample_text or "2.6 - 4T" in sample_text) and \
           ("GEO SEGMENT" in sample_text or "YEARS" in sample_text):
            return "cv_comp"
        
        # Default
        return "cv_comp"


# ===============================================================================
# CV COMP PROCESSOR
# ===============================================================================

class CVCompProcessor:
    """Process CV COMP sheets."""
    
    @staticmethod
    def process(content: bytes, sheet_name: str,
                override_enabled: bool = False,
                override_lob: str = None,
                override_segment: str = None) -> List[Dict]:
        """
        Process CV COMP pattern:
        Row 1: Title (JAN 2025 CV)
        Row 2: Geo Segments | Geo Segment CV | 2.6 - 4T columns
        Row 3: (empty) | (empty) | New | >1 - 5 Years | >5 - 10+ Years | New
        Row 5+: Data rows
        """
        records = []
        
        try:
            df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
            print(f"\n[CV_COMP] Processing sheet: {sheet_name}")
            print(f"[CV_COMP] Sheet shape: {df.shape}")
            
            # Find header row with "Geo Segments"
            header_row = None
            for i in range(min(10, df.shape[0])):
                row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
                if "GEO SEGMENT" in row_text:
                    header_row = i
                    break
            
            if header_row is None:
                print("[CV_COMP] Header row not found")
                return records
            
            print(f"[CV_COMP] Found header row at index: {header_row}")
            
            # Next row might have age bands (New, >1-5 Years, etc.)
            age_row = header_row + 1
            
            # Data starts after age row
            data_start = age_row + 1
            for i in range(data_start, df.shape[0]):
                if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
                    data_start = i
                    break
            
            print(f"[CV_COMP] Age row: {age_row}, Data starts: {data_start}")
            
            # Build column metadata (first two columns are Geo Segments and Geo Segment CV)
            col_meta = []
            for col_idx in range(2, df.shape[1]):
                tonnage = cell_to_str(df.iloc[header_row, col_idx])
                age_band = cell_to_str(df.iloc[age_row, col_idx])
                
                if not tonnage and not age_band:
                    continue
                
                # Build segment description
                segment_desc = ""
                if tonnage:
                    segment_desc = tonnage
                if age_band:
                    segment_desc += f" ({age_band})" if segment_desc else age_band
                
                col_meta.append({
                    "col_idx": col_idx,
                    "tonnage": tonnage,
                    "age_band": age_band,
                    "segment_desc": segment_desc,
                })
            
            if not col_meta:
                print("[CV_COMP] No data columns found")
                return records
            
            print(f"[CV_COMP] Found {len(col_meta)} columns")
            for m in col_meta[:5]:
                print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
            # Process data rows
            lob_final = override_lob if override_enabled and override_lob else "CV"
            segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
            skip_words = {"total", "grand total", "average", "sum", ""}
            
            for row_idx in range(data_start, df.shape[0]):
                geo_segments = cell_to_str(df.iloc[row_idx, 0])
                geo_segment_cv = cell_to_str(df.iloc[row_idx, 1])
                
                if not geo_segments and not geo_segment_cv:
                    continue
                
                if geo_segments.lower() in skip_words:
                    continue
                
                # Combine both geo columns
                combined_location = f"{geo_segments} - {geo_segment_cv}" if geo_segments and geo_segment_cv else (geo_segments or geo_segment_cv)
                
                # Extract state
                state = map_state(geo_segment_cv if geo_segment_cv else geo_segments)
                
                # Process each column
                for m in col_meta:
                    payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
                    if payin is None or payin == 0:
                        continue
                    
                    payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
                    records.append({
                        "State": state,
                        "Geo Location": combined_location,
                        "Geo Segments": geo_segments,
                        "Geo Segment CV": geo_segment_cv,
                        "Original Segment": m["segment_desc"],
                        "Tonnage": m["tonnage"],
                        "Age Band": m["age_band"],
                        "Mapped Segment": segment_final,
                        "LOB": lob_final,
                        "Status": "STP",
                        "Payin": f"{payin:.2f}%",
                        "Payin Category": get_payin_category(payin),
                        "Calculated Payout": f"{payout:.2f}%",
                        "Formula Used": formula,
                        "Rule Explanation": explanation,
                    })
            
            print(f"[CV_COMP] Extracted {len(records)} records")
            return records
            
        except Exception as e:
            print(f"[CV_COMP] Error: {e}")
            traceback.print_exc()
            return []


# ===============================================================================
# CV COMP TONNAGE-AGE PROCESSOR
# ===============================================================================

class CVCompTonnageAgeProcessor:
    """Process CV COMP sheets with tonnage ranges and age bands."""
    
    @staticmethod
    def process(content: bytes, sheet_name: str,
                override_enabled: bool = False,
                override_lob: str = None,
                override_segment: str = None) -> List[Dict]:
        """
        Process CV COMP with tonnage-age pattern:
        Row 2: 0 - 2.5T | 2.5 - 3.5T | 3.5 - 7.5T
        Row 3: Geo Location - New | New | >1 - 5 Years | >5 - 10+ Years | New | >1 - 5 Years | ...
        Row 5+: Data rows
        """
        records = []
        
        try:
            df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
            print(f"\n[CV_COMP_TONNAGE_AGE] Processing sheet: {sheet_name}")
            print(f"[CV_COMP_TONNAGE_AGE] Sheet shape: {df.shape}")
            
            # Find tonnage row (0 - 2.5T, 2.5 - 3.5T, etc.)
            tonnage_row = None
            for i in range(min(10, df.shape[0])):
                row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
                if ("2.5T" in row_text or "3.5T" in row_text or "7.5T" in row_text) and "-" in row_text:
                    tonnage_row = i
                    break
            
            if tonnage_row is None:
                print("[CV_COMP_TONNAGE_AGE] Tonnage row not found")
                return records
            
            print(f"[CV_COMP_TONNAGE_AGE] Found tonnage row at index: {tonnage_row}")
            
            # Age band row is next
            age_row = tonnage_row + 1
            
            # Find data start (look for "Geo Location - New" or first location)
            data_start = age_row + 1
            for i in range(data_start, df.shape[0]):
                if cell_to_str(df.iloc[i, 0]):
                    data_start = i
                    break
            
            print(f"[CV_COMP_TONNAGE_AGE] Age row: {age_row}, Data starts: {data_start}")
            
            # Build column metadata (combine tonnage + age)
            # Column 0 is "Geo Location - New"
            col_meta = []
            last_tonnage = ""
            
            for col_idx in range(1, df.shape[1]):
                tonnage = cell_to_str(df.iloc[tonnage_row, col_idx])
                age_band = cell_to_str(df.iloc[age_row, col_idx])
                
                # Forward fill tonnage (for merged cells)
                if tonnage:
                    last_tonnage = tonnage
                
                if not age_band:
                    continue
                
                # Build combined segment
                segment_desc = f"{last_tonnage} ({age_band})" if last_tonnage else age_band
                
                col_meta.append({
                    "col_idx": col_idx,
                    "tonnage": last_tonnage,
                    "age_band": age_band,
                    "segment_desc": segment_desc,
                })
            
            if not col_meta:
                print("[CV_COMP_TONNAGE_AGE] No data columns found")
                return records
            
            print(f"[CV_COMP_TONNAGE_AGE] Found {len(col_meta)} columns")
            for m in col_meta[:5]:
                print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
            # Process data rows
            lob_final = override_lob if override_enabled and override_lob else "CV"
            segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
            skip_words = {"total", "grand total", "average", "sum", ""}
            
            for row_idx in range(data_start, df.shape[0]):
                geo_location = cell_to_str(df.iloc[row_idx, 0])
                
                if not geo_location or geo_location.lower() in skip_words:
                    continue
                
                state = map_state(geo_location)
                
                # Process each column
                for m in col_meta:
                    payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
                    if payin is None or payin == 0:
                        continue
                    
                    payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
                    records.append({
                        "State": state,
                        "Geo Location": geo_location,
                        "Original Segment": m["segment_desc"],
                        "Tonnage": m["tonnage"],
                        "Age Band": m["age_band"],
                        "Mapped Segment": segment_final,
                        "LOB": lob_final,
                        "Status": "STP",
                        "Payin": f"{payin:.2f}%",
                        "Payin Category": get_payin_category(payin),
                        "Calculated Payout": f"{payout:.2f}%",
                        "Formula Used": formula,
                        "Rule Explanation": explanation,
                    })
            
            print(f"[CV_COMP_TONNAGE_AGE] Extracted {len(records)} records")
            return records
            
        except Exception as e:
            print(f"[CV_COMP_TONNAGE_AGE] Error: {e}")
            traceback.print_exc()
            return []


# ===============================================================================
# CV SATP PROCESSOR
# ===============================================================================

class CVSATPProcessor:
    """Process CV SATP sheets."""
    
    @staticmethod
    def process(content: bytes, sheet_name: str,
                override_enabled: bool = False,
                override_lob: str = None,
                override_segment: str = None) -> List[Dict]:
        """
        Process CV SATP pattern:
        Row 1: Title (JAN 2025 PAYOUT_CV SATP)
        Row 2: Segment | Upto 2.5 Ton GCV 4W GCV 3W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
        Row 3: Geo Location - New | (empty or merged)
        Row 5+: Data rows
        """
        records = []
        
        try:
            df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
            print(f"\n[CV_SATP] Processing sheet: {sheet_name}")
            print(f"[CV_SATP] Sheet shape: {df.shape}")
            
            # Find the "Segment" row (contains tonnage categories)
            segment_row = None
            geo_row = None
            
            for i in range(min(10, df.shape[0])):
                row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
                first_cell = cell_to_str(df.iloc[i, 0]).upper()
                
                # Row with "SEGMENT" (or typo "SEGEMENT") in first column
                # Check if other columns have tonnage data
                if ("SEGMENT" in first_cell or "SEGEMENT" in first_cell):
                    # Check if this row or next row has tonnage info
                    has_tonnage = False
                    for j in range(1, min(6, df.shape[1])):
                        cell_val = cell_to_str(df.iloc[i, j]).upper()
                        if cell_val and ("TON" in cell_val or "GCV" in cell_val or "PCV" in cell_val or "T" in cell_val):
                            has_tonnage = True
                            break
                    
                    if has_tonnage:
                        segment_row = i
                        print(f"[CV_SATP] Found segment row at index: {i}")
                
                # Row with "GEO LOCATION" in first column
                if "GEO LOCATION" in first_cell:
                    geo_row = i
                    print(f"[CV_SATP] Found geo row at index: {i}")
            
            if segment_row is None:
                print("[CV_SATP] Segment row not found")
                print("[CV_SATP] First 10 rows:")
                for i in range(min(10, df.shape[0])):
                    print(f"  Row {i} Col 0: '{cell_to_str(df.iloc[i, 0])}'")
                    if df.shape[1] > 1:
                        print(f"    Col 1: '{cell_to_str(df.iloc[i, 1])}'")
                return records
            
            print(f"[CV_SATP] Using segment row: {segment_row}")
            
            # Build column metadata from segment row AND geo row (they might be split)
            # Row 1: Segement | Upto 2.5 Ton | >2.5~3.5 T | >3.5~7.5 T | PCV 3W
            # Row 2: Geo Location - New | GCV 4W | (empty) | (empty) | Autorickshaw
            # Combined: Upto 2.5 Ton GCV 4W | >2.5~3.5 T | >3.5~7.5 T | PCV 3W Autorickshaw
            
            col_meta = []
            for col_idx in range(1, df.shape[1]):
                segment_part1 = cell_to_str(df.iloc[segment_row, col_idx])
                segment_part2 = ""
                
                # If we have a geo_row, try to get second part of header
                if geo_row is not None and geo_row > segment_row:
                    segment_part2 = cell_to_str(df.iloc[geo_row, col_idx])
                
                # Combine both parts
                if segment_part1 and segment_part2:
                    combined_segment = f"{segment_part1} {segment_part2}".strip()
                elif segment_part1:
                    combined_segment = segment_part1.strip()
                elif segment_part2:
                    combined_segment = segment_part2.strip()
                else:
                    continue
                
                if not combined_segment:
                    continue
                
                col_meta.append({
                    "col_idx": col_idx,
                    "segment": combined_segment,
                })
            
            if not col_meta:
                print("[CV_SATP] No data columns found")
                print(f"[CV_SATP] Segment row content:")
                for col_idx in range(df.shape[1]):
                    print(f"  Col {col_idx}: '{cell_to_str(df.iloc[segment_row, col_idx])}'")
                if geo_row is not None:
                    print(f"[CV_SATP] Geo row content:")
                    for col_idx in range(df.shape[1]):
                        print(f"  Col {col_idx}: '{cell_to_str(df.iloc[geo_row, col_idx])}'")
                return records
            
            # Data starts after geo_row (or segment_row + 1 if no geo_row found)
            if geo_row is not None:
                data_start = geo_row + 1
            else:
                data_start = segment_row + 1
            
            # Skip empty rows
            for i in range(data_start, df.shape[0]):
                if cell_to_str(df.iloc[i, 0]):
                    data_start = i
                    break
            
            print(f"[CV_SATP] Data starts at row: {data_start}")
            
            print(f"[CV_SATP] Found {len(col_meta)} columns:")
            for m in col_meta:
                print(f"  - Col {m['col_idx']}: '{m['segment']}'")
            
            # Process data rows
            lob_final = override_lob if override_enabled and override_lob else "CV"
            segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
            skip_words = {"total", "grand total", "average", "sum", ""}
            
            processed_count = 0
            for row_idx in range(data_start, df.shape[0]):
                geo_location = cell_to_str(df.iloc[row_idx, 0])
                
                if not geo_location or geo_location.lower() in skip_words:
                    continue
                
                state = map_state(geo_location)
                
                # Process each column
                for m in col_meta:
                    payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
                    if payin is None or payin == 0:
                        continue
                    
                    payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
                    records.append({
                        "State": state,
                        "Geo Location": geo_location,
                        "Original Segment": m["segment"],
                        "Mapped Segment": segment_final,
                        "LOB": lob_final,
                        "Status": "STP",
                        "Payin": f"{payin:.2f}%",
                        "Payin Category": get_payin_category(payin),
                        "Calculated Payout": f"{payout:.2f}%",
                        "Formula Used": formula,
                        "Rule Explanation": explanation,
                    })
                    processed_count += 1
            
            print(f"[CV_SATP] Extracted {len(records)} records from {processed_count} data points")
            return records
            
        except Exception as e:
            print(f"[CV_SATP] Error: {e}")
            traceback.print_exc()
            return []


# ===============================================================================
# CV SATP GEO NEW/OLD PROCESSOR
# ===============================================================================

class CVSATPGeoNewOldProcessor:
    """Process CV SATP sheets with Geo New/Old + tonnage + age bands."""
    
    @staticmethod
    def process(content: bytes, sheet_name: str,
                override_enabled: bool = False,
                override_lob: str = None,
                override_segment: str = None) -> List[Dict]:
        """
        Process CV SATP Geo New/Old pattern:
        Row 2: Title (March 2025  PAYOUT - CVSATP)
        Row 4: Upto 2.5 Ton GCV 4W | >2.5-3.5 Ton | >3.5~7.5 Ton | PCV 3W Autorickshaw | 12 - 20T
        Row 5: Geo segment New | Geo segment Old | New | >1-5 Years | >5-10+ Years | GCV 3W | (empty) | (empty) | (empty) | New | >1-5 Years
        Row 7+: Data
        """
        records = []
        
        try:
            df = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
            
            print(f"\n[CV_SATP_GEO_NEW_OLD] Processing sheet: {sheet_name}")
            print(f"[CV_SATP_GEO_NEW_OLD] Sheet shape: {df.shape}")
            
            # Find tonnage row (Upto 2.5 Ton, >2.5-3.5 Ton, etc.)
            tonnage_row = None
            for i in range(min(10, df.shape[0])):
                row_text = " ".join(cell_to_str(v) for v in df.iloc[i]).upper()
                if ("TON" in row_text or "GCV" in row_text or "PCV" in row_text or "20T" in row_text) and \
                   ("2.5" in row_text or "3.5" in row_text or "7.5" in row_text or "AUTORICKSHAW" in row_text):
                    # Make sure it's not the geo row
                    first_cell = cell_to_str(df.iloc[i, 0]).upper()
                    if "GEO" not in first_cell:
                        tonnage_row = i
                        break
            
            if tonnage_row is None:
                print("[CV_SATP_GEO_NEW_OLD] Tonnage row not found")
                return records
            
            print(f"[CV_SATP_GEO_NEW_OLD] Found tonnage row at index: {tonnage_row}")
            
            # Geo/Age row is next
            geo_age_row = tonnage_row + 1
            
            # Data starts after geo_age_row
            data_start = geo_age_row + 1
            for i in range(data_start, df.shape[0]):
                if cell_to_str(df.iloc[i, 0]) or cell_to_str(df.iloc[i, 1]):
                    data_start = i
                    break
            
            print(f"[CV_SATP_GEO_NEW_OLD] Geo/Age row: {geo_age_row}, Data starts: {data_start}")
            
            # Build column metadata (first two columns are Geo New and Geo Old)
            # Combine tonnage + age/subcategory
            col_meta = []
            last_tonnage = ""
            
            for col_idx in range(2, df.shape[1]):
                tonnage = cell_to_str(df.iloc[tonnage_row, col_idx])
                subcategory = cell_to_str(df.iloc[geo_age_row, col_idx])
                
                # Forward fill tonnage (for merged cells)
                if tonnage:
                    last_tonnage = tonnage
                
                if not subcategory:
                    continue
                
                # Build combined segment
                segment_desc = f"{last_tonnage} ({subcategory})" if last_tonnage else subcategory
                
                col_meta.append({
                    "col_idx": col_idx,
                    "tonnage": last_tonnage,
                    "subcategory": subcategory,
                    "segment_desc": segment_desc,
                })
            
            if not col_meta:
                print("[CV_SATP_GEO_NEW_OLD] No data columns found")
                print(f"[CV_SATP_GEO_NEW_OLD] Tonnage row: {[cell_to_str(df.iloc[tonnage_row, i]) for i in range(min(12, df.shape[1]))]}")
                print(f"[CV_SATP_GEO_NEW_OLD] Geo/Age row: {[cell_to_str(df.iloc[geo_age_row, i]) for i in range(min(12, df.shape[1]))]}")
                return records
            
            print(f"[CV_SATP_GEO_NEW_OLD] Found {len(col_meta)} columns:")
            for m in col_meta[:8]:
                print(f"  - Col {m['col_idx']}: {m['segment_desc']}")
            
            # Process data rows
            lob_final = override_lob if override_enabled and override_lob else "CV"
            segment_final = override_segment if override_enabled and override_segment else "All GVW & PCV 3W, GCV 3W"
            
            skip_words = {"total", "grand total", "average", "sum", ""}
            
            for row_idx in range(data_start, df.shape[0]):
                geo_new = cell_to_str(df.iloc[row_idx, 0])
                geo_old = cell_to_str(df.iloc[row_idx, 1])
                
                if not geo_new and not geo_old:
                    continue
                
                if geo_new.lower() in skip_words and geo_old.lower() in skip_words:
                    continue
                
                # Use whichever is available
                if not geo_new:
                    geo_new = geo_old
                if not geo_old:
                    geo_old = geo_new
                
                # Combine locations
                combined_location = f"{geo_new} - {geo_old}" if geo_new != geo_old else geo_new
                state = map_state(geo_old if geo_old else geo_new)
                
                # Process each column
                for m in col_meta:
                    payin = safe_float(df.iloc[row_idx, m["col_idx"]])
                    
                    if payin is None or payin == 0:
                        continue
                    
                    payout, formula, explanation = calculate_payout(payin, lob_final, segment_final)
                    
                    records.append({
                        "State": state,
                        "Geo Location": combined_location,
                        "Geo New": geo_new,
                        "Geo Old": geo_old,
                        "Original Segment": m["segment_desc"],
                        "Tonnage": m["tonnage"],
                        "Subcategory": m["subcategory"],
                        "Mapped Segment": segment_final,
                        "LOB": lob_final,
                        "Status": "STP",
                        "Payin": f"{payin:.2f}%",
                        "Payin Category": get_payin_category(payin),
                        "Calculated Payout": f"{payout:.2f}%",
                        "Formula Used": formula,
                        "Rule Explanation": explanation,
                    })
            
            print(f"[CV_SATP_GEO_NEW_OLD] Extracted {len(records)} records")
            return records
            
        except Exception as e:
            print(f"[CV_SATP_GEO_NEW_OLD] Error: {e}")
            traceback.print_exc()
            return []


# ===============================================================================
# PATTERN DISPATCHER
# ===============================================================================

class CVPatternDispatcher:
    """Route to correct CV processor."""
    
    PATTERN_PROCESSORS = {
        "cv_comp": CVCompProcessor,
        "cv_comp_tonnage_age": CVCompTonnageAgeProcessor,
        "cv_satp": CVSATPProcessor,
        "cv_satp_geo_new_old": CVSATPGeoNewOldProcessor,
    }
    
    @staticmethod
    def process_sheet(content: bytes, sheet_name: str,
                      override_enabled: bool = False,
                      override_lob: str = None,
                      override_segment: str = None) -> List[Dict]:
        """Detect pattern and route to processor."""
        df_raw = pd.read_excel(io.BytesIO(content), sheet_name=sheet_name, header=None)
        pattern = CVPatternDetector.detect_pattern(df_raw)
        
        print(f"\n[DISPATCHER] Detected pattern: {pattern}")
        
        processor_class = CVPatternDispatcher.PATTERN_PROCESSORS.get(pattern, CVCompProcessor)
        return processor_class.process(
            content, sheet_name,
            override_enabled, override_lob, override_segment
        )


# ===============================================================================
# API ENDPOINTS
# ===============================================================================

@app.get("/")
async def root():
    return {
        "message": "Carrying Vehicles Payout Processor API",
        "version": "3.0.0",
        "formula": "Tiered deduction based on payin ranges (independent of policy type)",
        "supported_lobs": ["CV"],
        "supported_segments": ["All GVW & PCV 3W, GCV 3W"],
        "supported_patterns": [
            "cv_comp - CV COMP (Geo Segments | Geo Segment CV | Age bands)",
            "cv_comp_tonnage_age - CV COMP with tonnage ranges + age bands",
            "cv_satp - CV SATP (Segment | Geo Location - New | Tonnage categories)",
            "cv_satp_geo_new_old - CV SATP with Geo New/Old + tonnage + age bands"
        ],
        "formula_tiers": [
            "Payin ≤ 20%: -2%",
            "Payin 21-30%: -3%",
            "Payin 31-50%: -4%",
            "Payin > 50%: -5%"
        ]
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload Excel file."""
    try:
        if not file.filename.endswith((".xlsx", ".xls")):
            raise HTTPException(status_code=400, detail="Only Excel files supported")
        
        content = await file.read()
        xls = pd.ExcelFile(io.BytesIO(content))
        sheets = xls.sheet_names
        
        file_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        uploaded_files[file_id] = {
            "content": content,
            "filename": file.filename,
            "sheets": sheets,
        }
        
        return {
            "file_id": file_id,
            "filename": file.filename,
            "sheets": sheets,
            "message": f"Uploaded successfully. {len(sheets)} worksheet(s) found.",
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


@app.post("/process")
async def process_sheet(
    file_id: str,
    sheet_name: str,
    override_enabled: bool = False,
    override_lob: Optional[str] = None,
    override_segment: Optional[str] = None,
):
    """Process worksheet."""
    try:
        if file_id not in uploaded_files:
            raise HTTPException(status_code=404, detail="File not found")
        
        file_data = uploaded_files[file_id]
        
        if sheet_name not in file_data["sheets"]:
            raise HTTPException(status_code=400, detail=f"Sheet '{sheet_name}' not found")
        
        records = CVPatternDispatcher.process_sheet(
            file_data["content"], 
            sheet_name,
            override_enabled, 
            override_lob, 
            override_segment,
        )
        
        if not records:
            return {
                "success": False,
                "message": "No records extracted. Check sheet structure.",
                "records": [],
                "count": 0,
            }
        
        # Summary stats
        states = {}
        payins = []
        payouts = []
        
        for r in records:
            state = r.get("State", "UNKNOWN")
            states[state] = states.get(state, 0) + 1
            
            try:
                payin_val = float(r.get("Payin", "0%").replace("%", ""))
                payout_val = float(r.get("Calculated Payout", "0%").replace("%", ""))
                payins.append(payin_val)
                payouts.append(payout_val)
            except Exception:
                pass
        
        avg_payin = round(sum(payins) / len(payins), 2) if payins else 0
        avg_payout = round(sum(payouts) / len(payouts), 2) if payouts else 0
        
        return {
            "success": True,
            "message": f"Successfully processed {len(records)} records from '{sheet_name}'",
            "records": records,
            "count": len(records),
            "summary": {
                "total_records": len(records),
                "states": dict(sorted(states.items(), key=lambda x: x[1], reverse=True)[:10]),
                "average_payin": avg_payin,
                "average_payout": avg_payout,
            },
        }
        
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


@app.post("/export")
async def export_to_excel(file_id: str, sheet_name: str, records: List[Dict]):
    """Export to Excel."""
    try:
        if not records:
            raise HTTPException(status_code=400, detail="No records to export")
        
        df = pd.DataFrame(records)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"CV_Processed_{sheet_name.replace(' ', '_')}_{timestamp}.xlsx"
        out_path = os.path.join(tempfile.gettempdir(), filename)
        
        with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name="Processed Data")
            
            worksheet = writer.sheets["Processed Data"]
            for idx, col in enumerate(df.columns):
                max_length = max(
                    df[col].astype(str).apply(len).max(),
                    len(str(col))
                )
                worksheet.column_dimensions[chr(65 + idx)].width = min(max_length + 2, 50)
        
        return FileResponse(
            path=out_path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uploaded_files": len(uploaded_files)
    }


if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 70)
    print("Carrying Vehicles Payout Processor API - v3.0.0")
    print("Patterns: CV COMP + CV COMP Tonnage-Age + CV SATP + CV SATP Geo New/Old")
    print("Formula: Independent of policy type, tiered deductions")
    print("=" * 70 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
