# Gadgettissimo Gestionale · v1.7

Prima versione funzionante per negozio, installazione locale e accesso via browser. **È una prima release modulare, non l’intero gestionale descritto nel prompt master.** Dati persistenti, archivio iniziale vuoto, nessuna credenziale preimpostata.

## Inizia su Windows 10 / 11

1. Installa **Python 3.12 o 3.13 a 64 bit** da https://www.python.org/downloads/windows/ e seleziona **Add Python to PATH**. Python 3.12 è la versione verificata qui.
2. Estrai tutto lo ZIP in una cartella scrivibile del tuo utente, ad esempio `Documenti\Gadgettissimo`. Non avviarlo dentro lo ZIP o in Program Files.
3. Con Internet attivo, doppio clic su **Installa-Windows.cmd**. Non servono Node.js o comandi manuali: l’interfaccia compilata è già inclusa.
4. Doppio clic su **Avvia-Gadgettissimo.cmd**. Il browser si apre su http://127.0.0.1:8765.
5. Al primo avvio crea il tuo amministratore con una password di almeno 12 caratteri. Completa il primo avvio sul PC locale prima di abilitare la rete.

**Guida per il negozio:** apri `Apri-Guida.cmd` oppure [docs/GUIDA.html](docs/GUIDA.html). Per arrestare il programma chiudi la finestra di avvio o premi Ctrl+C. Il PC server deve restare acceso durante il lavoro delle altre postazioni.

## Novità 1.7: Ri.Ba. in Scadenze, allarmi e Google Calendar

- **Scadenza Ri.Ba. automatica:** quando confermi un arrivo con metodo Ri.Ba., il pagamento viene inserito in Scadenze con il residuo dovuto, la scadenza del carico e un avviso **7 giorni prima alle 09:00 italiane**. I carichi Ri.Ba. già confermati vengono recuperati durante l’aggiornamento. La bozza non genera un’obbligazione da pagare.
- **Collegamento al carico:** il pagamento parziale aggiorna il residuo; il saldo completa la scadenza. Modificare la data del carico aggiorna la stessa scadenza; annullarlo o passare a un altro metodo ritira quella collegata. Gli allarmi personalizzati vengono conservati. Per queste scadenze data/importo/completamento si gestiscono dal carico, senza registrare due volte il pagamento.
- **Allarme configurabile per tutte le scadenze:** apri Nuova/Modifica scadenza e scegli da **0 a 28 giorni prima**, l’orario italiano oppure Nessun allarme. Puoi cambiare l’allarme anche su una Ri.Ba. collegata.
- **Messaggio e campanella:** un riepilogo compare mentre usi il gestionale; la campanella apre gli avvisi con importo e accesso al carico. **Ricordamelo domani** rinvia l’avviso solo per il tuo account. Le notifiche native del browser sono facoltative e richiedono consenso, browser compatibile e normalmente HTTPS o accesso locale. Funzionano mentre la pagina è aperta.
- **Google Calendar:** in Scadenze trovi il collegamento al tuo account e il calendario dedicato **Gadgettissimo – Scadenze**. Il server invia le scadenze e aggiorna/ritira gli eventi ogni minuto; modifica date e pagamenti nel gestionale. Google può ricordarli anche ad app chiusa, se hai abilitato le sue notifiche e gli eventi sono già sincronizzati. La prima attivazione richiede le credenziali OAuth del tuo progetto Google sul server e il tuo consenso: nessun account è precollegato nello ZIP.

Per attivare Google apri **Scadenze → Google Calendar → Guida di attivazione** come amministratore, oppure [docs/Google-Calendar.html](docs/Google-Calendar.html). La guida include Google Cloud, URI locale/VPS HTTPS, configurazione `.env`, autorizzazione e prova degli avvisi. Il gestionale richiede il permesso limitato ai calendari creati dall’app; non importa gli eventi personali o le modifiche eseguite su Google. Dopo un ripristino di backup occorre ricollegare Google; scadenze e preferenze degli allarmi restano nel database.

## Novità 1.6: arrivi modificabili, Ri.Ba. e clienti con listino

- **Arrivi merce:** dalla scheda premi **Modifica arrivo**, anche dopo la conferma. Correggi fornitore, riferimento, data, note, magazzino, righe, quantità e costi. Per un confermato spunta la conferma di rettifica: il magazzino cambia per la differenza e l’ultimo costo viene ricalcolato dal carico confermato più recente. Una modifica alle sole note non cambia il costo.
- **Elimina arrivo:** disponibile per bozze e confermati, con conferma dello storno della merce. Il documento rimane in **Arrivi rimossi** con righe, pagamenti e storico. La merce da togliere deve essere ancora disponibile nel magazzino. Se il carico è pagato, registra il rimborso già ricevuto dal fornitore; se riduci il totale sotto il pagato, serve il rimborso della differenza. Queste registrazioni richiedono Cassa e una sessione aperta. Il fornitore di un carico già pagato non si cambia: occorre annullare con rimborso e ricreare.
- **Ri.Ba. 30/60 giorni fine mese:** nel pagamento fornitore scegli Ri.Ba. e la condizione. Regola concordata: ultimo giorno del mese successivo o del secondo mese successivo alla data del documento; senza data documento usa il giorno di creazione italiano. Esempio 14/11/2026 → 31/12/2026 oppure 31/01/2027. La scadenza è visibile nella scheda, elenco arrivi e PDF, e può essere corretta. Scegliere Ri.Ba. non registra un’uscita: registra il pagamento quando avviene l’addebito, salvo esplicita spunta di pagamento alla conferma. Non vengono generate rate. Dalla 1.7 i carichi Ri.Ba. confermati creano automaticamente la scadenza collegata con allarme.
- **Cassa senza fondo iniziale:** premi Apri cassa e conferma; le nuove sessioni partono da zero. Spese, pagamenti ai fornitori, prelievi e rimborsi in contanti sono ammessi anche con saldo contabile negativo. Restano obbligatori permessi, importi validi e sessione aperta. Le vecchie sessioni, comprese quelle già aperte all’aggiornamento, conservano i valori storici; il saldo iniziale precedente viene indicato quando presente.
- **Cliente pubblico o rivenditore:** in **Clienti → Nuovo/Modifica → Tipo cliente / listino** scegli la classificazione. I clienti già presenti partono da Pubblico. Nel nuovo ordine o preventivo seleziona il cliente: il listino si imposta automaticamente e ricalcola i prezzi automatici già inseriti, comprese le soglie quantità. Puoi scegliere un listino diverso; i prezzi manuali restano manuali. I documenti salvati mantengono prezzi e regole storiche anche se cambi il tipo del cliente. Nell’editor degli ordini del gestionale principale puoi scegliere un altro cliente dall’anagrafica. Il banco mantiene il proprio selettore listino.

**Costo, uscita e rimborso:** il costo è registrato dal carico confermato; il pagamento fornitore è un’uscita `SUPPLIER_PAYMENT`; il rimborso ricevuto è un’entrata `SUPPLIER_REFUND`. In **Incassi e statistiche → Entrate e uscite → Pagamenti e rimborsi fornitori** trovi entrambi, filtrabili per direzione, metodo e data. Nessuna registrazione esegue trasferimenti bancari reali. Le revisioni e i doppi invii sono controllati; ogni errore annulla l’intera rettifica.

## Novità 1.5: foto multiple, listini e ordini correggibili

- **Tema scuro:** testi, campi, menu, pulsanti, tabelle e stati con colori più leggibili.
- **Finestre:** il clic all’esterno non chiude nulla. X, Esc ed **Esci** chiedono conferma; **Salva** chiude dopo il salvataggio riuscito. Durante il salvataggio non puoi chiudere la finestra.
- **Foto già nella creazione:** nella scheda del nuovo prodotto premi **Aggiungi foto**, anche selezionando più file. Massimo 10 foto JPG/PNG/WebP, 5 MB/20 MP ciascuna. Si collegano al prodotto quando salvi. La prima è la principale; puoi cambiarla o rimuovere foto. Per un prodotto già esistente le modifiche alla galleria sono immediate.
- **Prezzi per variante:** prezzo pubblico e rivenditore IVA inclusa; se il rivenditore è vuoto usa il pubblico. La tabella **Prezzi in base alla quantità** consente fino a 20 soglie per listino (es. pubblico da 5 pezzi → 9 €, da 10 → 8 €). Al banco, negli ordini e nei preventivi scegli il listino: cambia la quantità e si applica la soglia raggiunta. Le soglie valgono per singola riga/variante, senza sommare taglie o colori diversi. Un prezzo scritto manualmente resta manuale. Gli ordini conservano le regole del momento della creazione; i successivi cambi al catalogo non modificano i prezzi storici.
- **Ordini anche consegnati:** apri l’ordine → **Modifica ordine / operatori**. Per un consegnato conferma la rettifica. Se cambia il totale indica il metodo dell’incasso aggiuntivo o del rimborso; servono permesso Cassa e sessione aperta. Il magazzino viene rettificato solo per la differenza e l’ordine resta Consegnato. La correzione dei ricavi viene registrata oggi, conservando lo storico precedente. Il portale Operatori continua a modificare soltanto gli ordini aperti assegnati.
- **Rimuovi ordine:** disponibile anche con acconti e dopo la consegna. La conferma registra il rimborso degli importi ricevuti, restituisce lo stock eventualmente scaricato e storna i ricavi. L’ordine resta consultabile in **Ordini rimossi**, con storico e audit. Nessuna operazione bancaria viene eseguita dall’app: registra il rimborso dopo averlo effettuato.
- **Pagamento al fornitore all’arrivo:** scegli metodo e importo nel nuovo carico. Spunta **Registra il pagamento e l’uscita quando confermo il carico** soltanto se stai effettivamente pagando; conferma carico, stock e pagamento avvengono insieme. Senza spunta, il carico registra il costo e lascia il debito aperto. Puoi pagare successivamente, anche in parte, dalla scheda del carico.

**Dove vedo l’uscita del carico?** In **Incassi e statistiche → Entrate e uscite**, seleziona **Solo uscite** e tipo **Pagamenti fornitori**, con il periodo della data del pagamento. Nella scheda del carico trovi pagato, saldo e **Vedi l’uscita in Entrate e uscite**. Se hai soltanto confermato la merce, senza registrare il pagamento, vedrai il costo in **Carichi merce · costi di acquisto** e nessuna uscita finanziaria: costo e pagamento rimangono distinti.

## Novità 1.4: foto, catalogo, marchio e movimenti finanziari

- **Foto prodotto:** usa Aggiungi foto già nella creazione, la fotocamera sulla riga o la modifica del prodotto. Carica/cambia/rimuovi JPG, PNG o WebP (5 MB, 20 megapixel). La foto è comune alle varianti, visibile nel catalogo a video e al banco; viene ridimensionata e salvata nel database, quindi inclusa nei backup.
- **Stampa catalogo:** da Prodotti premi **Stampa catalogo**, scegli categoria/ricerca, foto, prezzi e soli attivi; apri l’anteprima o scarica il PDF A4. Include codici, taglie, colori e prezzi IVA inclusa, senza costi interni.
- **Logo del negozio:** caricalo in Impostazioni → Negozio e profilo. Compare su catalogo, documenti A4/80 mm, etichette e riepiloghi di cassa. I PNG trasparenti mantengono la trasparenza. Anche il logo è nel backup del database.
- **Prossimi ordini in alto:** il riquadro è subito sotto il titolo della Panoramica, prima del banner e degli altri indicatori. Le consegne datate precedono quelle senza data.
- **Incassi e statistiche:** vista Entrate e uscite con grafico, movimenti, ricerca, CSV e filtri per direzione, tipo, metodo e operatore. Periodi Oggi, Mensile (mese selezionabile), Scorso mese, Data specifica e intervallo libero. Rimane disponibile la vista Vendite e margini con gli stessi periodi.
- **Carichi e pagamenti distinti:** i carichi confermati compaiono come costi di acquisto, con importi pagati e ancora dovuti. Apri un carico confermato e premi **Registra pagamento fornitore**: anche un pagamento parziale diventa un’uscita effettiva, tracciata una sola volta nella cassa dell’operatore. Servono permessi Arrivi/Cassa e una sessione aperta; le uscite in contanti sono ammesse anche con saldo contabile negativo.

Il costo di un carico non è automaticamente un pagamento. I carichi precedenti vengono recuperati dalla loro conferma (o dalla creazione se manca lo storico), senza inventare uscite. Le uscite del periodo seguono la data dei pagamenti; il riepilogo acquisti segue la data di conferma e mostra il saldo aggiornato ad oggi. La differenza entrate/uscite riguarda movimenti finanziari, mentre il margine usa il costo storico della merce venduta.

## Novità 1.3: banco rapido, operatori e agenda

- **Sei caselle in alto nella Vendita al banco.** Scegli i prodotti/varianti più usati, richiamali con un clic e cambiali o svuotali con la matita. La scelta è condivisa tra le postazioni; prezzo e disponibilità sono letti dal catalogo e dal magazzino selezionato.
- **Sezione Operatori.** L’amministratore crea gli account, ne gestisce accesso e password. Gli ordini aperti si assegnano a una o più persone durante la creazione o da **Modifica / assegna** nella scheda ordine.
- **Accesso dedicato `/operatori`.** Ogni operatore vede esclusivamente gli ordini assegnati a lui, crea nuovi ordini assegnati automaticamente a sé, modifica righe e istruzioni, cambia stato e rimuove gli ordini senza incassi. L’elenco si aggiorna ogni 30 secondi. Gli ordini rimossi restano nello storico amministrativo; i consegnati possono essere rettificati dal responsabile nel gestionale principale. Acconti, saldi e rimborsi restano alla cassa.
- **Scadenze.** Titolo, data, tipo, descrizione e importo facoltativo; modifica, completamento, riapertura e rimozione. In dashboard compaiono le scadenze entro sette giorni e quelle scadute. Il completamento è un promemoria, non un pagamento.
- **Note al volo in dashboard.** Aggiungi con il pulsante o Ctrl+Invio, modifica e rimuovi. Le note sono personali e persistono sul database, accessibili dallo stesso account sulle altre postazioni.

Gli ordini aperti sono modificabili anche con acconti; se il nuovo totale scende sotto il pagato è richiesto il rimborso della differenza. Le modifiche sono tracciate; se un altro utente ha aggiornato l’ordine occorre ricaricarlo. Un ordine pronto modificato torna in lavorazione. Le quantità si scaricano soltanto alla consegna, dopo il saldo e il controllo di disponibilità. Nessuna cancellazione fisica degli ordini viene eseguita.

## Novità 1.2: catalogo e varianti in tabella

Il **codice articolo precede il nome** nei moduli, nel catalogo e nelle righe operative. Ogni variante ha un codice univoco in tutto l’archivio: `ABC123` e `abc123` sono lo stesso codice. Il campo vuoto di una nuova variante genera un codice libero.

**Categoria e sottocategoria si scelgono dagli elenchi.** Il pulsante **+** accanto a ciascun elenco aggiunge e seleziona una voce; le sottocategorie dipendono dalla categoria. Le categorie già usate vengono recuperate dall’archivio durante l’aggiornamento.

**Tabella varianti:** righe per taglia e colonne per colore con il pallino della tinta. Scegli Adulto (XS–XXXXL), Bambino (1–14 anni) o Taglia unica, premi **+ Aggiungi colore**, spunta le combinazioni e scrivi le quantità contate. Nella seconda tabella correggi codice, prezzo, costo, scorta minima e barcode. **Salva tabella** registra insieme tutte le modifiche, con movimenti di inventario tracciati. Il cambio fascia conserva le righe preparate. Il salvataggio si ferma se qualcuno ha modificato i dati o la giacenza che stai rettificando.

Le varianti e i documenti esistenti restano disponibili. Se l’archivio precedente contiene codici uguali per maiuscole/minuscole, la migrazione conserva il primo e distingue i successivi con `-DUP-ID`, registrando la correzione nell’audit. Gli snapshot dei documenti storici restano invariati. Le etichette dei codici corretti vanno ristampate.

Per aggiornare: chiudi il gestionale, estrai lo ZIP in una cartella diversa, avvia **Aggiorna-Windows.cmd** e scegli la cartella del gestionale esistente. Il sistema salva prima database e programmi, conserva `.env`, `.venv` e dati, applica la migrazione e ripristina il precedente stato se l’aggiornamento fallisce. Il database vuoto è allegato nello ZIP sotto `database-template`, evitando di sovrascrivere il percorso dei dati operativi. Consulta la guida per la procedura completa.

## Cosa puoi già fare

- Autenticazione con Argon2id, sessioni con scadenza di 8 ore, ruoli configurabili e registro operazioni.
- Prodotti, varianti con SKU e barcode univoci, prezzi e IVA, duplicazione, disattivazione, etichette Code128 PDF.
- Più magazzini, carichi/scarichi, inventario fisico e trasferimenti atomici; giacenze non negative.
- Clienti e fornitori con recapiti, dati fiscali e storico documenti.
- Vendite al banco con più righe, sconti per riga, pagamenti misti, ricerca barcode, riepiloghi A4 e 80 mm, reso integrale.
- Ordini con personalizzazioni, modifiche tracciate, assegnazione multipla agli operatori, acconti, saldo e scarico alla consegna.
- Arrivi merce in bozza, conferma con carico automatico e aggiornamento costo netto.
- Preventivi convertibili in ordini conservando le righe e i prezzi originari.
- Cassa per operatore, entrate/uscite, spese, contante teorico e contato, chiusure archiviate e PDF.
- Dashboard e statistiche che distinguono vendite, incassi, acconti, costi e margini; CSV dei movimenti.
- CSV catalogo con anteprima, controllo duplicati e importazione atomica; backup SQLite manuali/automatici e ripristino offline verificato.

Leggi [la matrice delle funzioni e delle verifiche](docs/FUNZIONI_E_TEST.md) per limiti e moduli successivi. Le stampe sono **interne e non fiscali**. SDI, XML FatturaPA, registratore telematico e sincronizzazione Flazio non sono implementati.

## Struttura

```text
backend/app/                 API, dominio, sicurezza, report e backup
backend/migrations/          Migrazione Alembic completa dello schema
backend/tests/               Test automatici delle operazioni critiche
frontend/src/                React + TypeScript + Tailwind e CSS personalizzato
frontend/dist/               Interfaccia compilata pronta per l’uso
database-template/           Database iniziale vuoto allegato allo ZIP
data/gadgettissimo.db         Database operativo creato all’installazione
tools/                      Installazione, ripristino e recupero password locali
windows/Gadgettissimo.iss    Definizione di installer Inno Setup (da compilare/verificare)
docs/                       Architettura, guida e stato delle funzioni
*.cmd                       Avvio e manutenzione con doppio clic su Windows
```

## Sviluppo / Linux

Richiede Python 3.12/3.13; Node.js 22.12+ solo per ricompilare l’interfaccia.

```sh
python -m venv .venv
# Linux/macOS: .venv/bin/python; Windows: .venv\Scripts\python.exe
.venv/bin/python -m pip install -r requirements-dev.txt
cd frontend
npm ci
npm run build
cd ..
.venv/bin/python run.py
```

Test: `python -m pytest`. Migrazioni: `python -m alembic upgrade head` dalla cartella principale, a programma spento e con backup prima di ogni aggiornamento. Per sviluppo frontend avvia anche `npm run dev` da `frontend`; Vite inoltra `/api` al backend su porta 8765. Non utilizzare il server Vite per l’esercizio del negozio.

Configurazione opzionale: copia `.env.example` in `.env`. Non condividere `.env`, database o backup in repository pubblici. Consulta [ARCHITETTURA.md](docs/ARCHITETTURA.md) per rete locale e PostgreSQL. La migrazione dati SQLite → PostgreSQL non è automatica.

## Verifiche e distribuzione

Verificato in Linux con Python 3.12 e Node 24: suite API/database, ripristino reale, migrazioni e build TypeScript/React. Il riepilogo esatto è in `docs/VERIFICA.txt`.

Windows 10/11, PowerShell, stampanti fisiche, scansori hardware e PostgreSQL non sono stati provati direttamente in questo ambiente. Il controllo visivo in un browser non è stato eseguito: gli strumenti browser richiesti dall’ambiente Sites non erano disponibili. Prima dell’uso quotidiano esegui il collaudo indicato nella guida su una copia vuota. Non è incluso un `.exe` compilato o firmato; è inclusa la definizione Inno Setup.
