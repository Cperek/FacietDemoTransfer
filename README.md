# 🎮 Faceit Demo Auto Transfer Tool

Automatyczne narzędzie do transferu i dekompresji plików demo CS2 z Faceit. Program automatycznie na żywo wykrywa nowe pliki `.zst` w wybranym folderz, dekompresuje je do formatu `.dem` i przenosi do folderu CS2.

## 🚀 Użycie

1. Plik .exe znajdziesz w folderze `FacietDemoTransfer/`

## 🎯 Jak używać

### Pierwsze uruchomienie:
1. Uruchom program
2. Naciśnij Enter
3. Podaj ścieżkę do folderu SOURCE (gdzie pojawiają się pliki .zst z Faceit)
   ```
   Przykład: E:\
   ```
4. Podaj ścieżkę do folderu CS2 (gdzie mają być zapisywane pliki .dem)
   ```
   Przykład: C:\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo
   ```

### Kolejne uruchomienia:
- Program zapamięta poprzednie ścieżki
- Możesz je zmienić odpowiadając `y` na pytanie o zmianę


## 🔄 Proces działania

1. **Monitoring** - Program monitoruje folder SOURCE co 5 sekund
2. **Wykrywanie** - Znajduje nowe pliki `.zst`
3. **Sprawdzanie stabilności** - Czeka 3 sekundy aby upewnić się, że plik jest w pełni pobrany
4. **Dekompresja** - Dekompresuje `.zst` do `.dem`
5. **Przenoszenie** - Zapisuje plik z czasową nazwą w folderze CS2
6. **Czyszczenie** - Usuwa oryginalny plik `.zst`

## 📝 Komunikaty programu

| Komunikat | Znaczenie |
|-----------|-----------|
| `[SCAN] Checking file:` | Program sprawdza znaleziony plik |
| `[NEW] Found new demo:` | Znaleziono nowy plik demo |
| `[WAIT] still downloading...` | Plik jest jeszcze pobierany |
| `[OK] Transferred to:` | Plik został pomyślnie zdekompresowany |
| `[DEL] Deleted original:` | Oryginalny plik został usunięty |
| `[ERR] Error processing:` | Wystąpił błąd podczas przetwarzania |

## ⚙️ Konfiguracja

### Automatyczne zapisywanie ustawień:
Program tworzy plik `config.json` z Twoimi ścieżkami:
```json
{
    "source": "E:\\",
    "destination": "C:\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo"
}
```

### Formatowanie nazw plików:
Pliki demo są zapisywane z nazwą:
```
demo_YYYY_MM_DD_HH_MM_SS.dem
```
Przykład: `demo_2025_10_16_17_50_45.dem`

## 🎮 Przykład użycia

```
=== Faceit Demo Auto Transfer Tool ===
Press Enter to start...

[OK] Loaded saved folders:
   Source: E:\
   Destination: C:\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo
Do you want to change them? (y/N): n

[INFO] Watching folder:
E:\

Press Ctrl + C to stop.

[SCAN] Checking file: 1-90ba3366-dbd1-4bb1-8966-ab00ea3f489a-1-1.dem.zst

[NEW] Found new demo: 1-90ba3366-dbd1-4bb1-8966-ab00ea3f489a-1-1.dem.zst
[OK] Transferred to: C:\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\demo_2025_10_16_17_50_45.dem
[DEL] Deleted original: E:\1-90ba3366-dbd1-4bb1-8966-ab00ea3f489a-1-1.dem.zst
```

## 🚪 Zatrzymywanie programu

Naciśnij `Ctrl + C` aby bezpiecznie zatrzymać program.
