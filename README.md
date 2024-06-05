1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Scraping Script**:
   ```bash
   python scrape_data.py
   ```
4. **Run the CSV Generation Script**:
   ```bash
   python create_csv.py
   ```
5. **Access the PostgreSQL Database**:
   - Ensure PostgreSQL is running and accessible.
   - Check the `save.py` file for database connection settings.
