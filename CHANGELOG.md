# Versione 1.7.0

- Scadenze Ri.Ba. collegate univocamente ai carichi confermati, recupero di quelle preesistenti, residuo/completamento/ritiro sincronizzati con pagamenti e rettifiche.
- Allarme configurabile 0–28 giorni e orario italiano; default Ri.Ba. 7 giorni alle 09:00. Avvisi nel gestionale, campanella, rinvio personale a domani e notifiche browser facoltative.
- Integrazione Google Calendar con calendario dedicato, OAuth con stato monouso/cookie/PKCE, token cifrati e configurazione server facoltativa. Sincronizzazione differita, eventi con avvisi e tentativi automatici senza bloccare le operazioni finanziarie.
- Migrazione d83f9a4b0517 dopo c72e8f3a9406; nuovi dati nei backup e collegamento Google disattivato dopo un ripristino.
- Ripristino SQLite: checkpoint e chiusura effettiva delle connessioni prima della sostituzione, affinché revoca sessioni e aggiornamenti preparati siano nel file ripristinato.
- Nuova dipendenza cryptography 50.0.2; verifica mirata della dipendenza e transitive senza vulnerabilità note. Verifiche e limiti in docs/VERIFICA.txt.

# Versione 1.6.0

- Modifica degli arrivi in bozza e confermati, con revisioni, audit, righe/costi e rettifiche aggregate di magazzino; ultimo costo dal carico confermato più recente.
- Eliminazione logica degli arrivi anche confermati: storno stock, rimborsi fornitori espliciti e archivio Arrivi rimossi. Blocco delle rettifiche con stock insufficiente e rollback completo.
- Ri.Ba. e condizioni 30gfm/60gfm, scadenza calcolata a fine mese successivo/secondo mese e modificabile; metodo nel ledger, report e stampe.
- Apertura cassa senza fondo; uscite in contanti consentite anche con saldo negativo, conservando sessioni e saldi precedenti.
- Classificazione clienti Pubblico/Rivenditore e selezione automatica dei prezzi nell’ordine/preventivo; conservazione di prezzi manuali e snapshot storici.
- Migrazione c72e8f3a9406 dopo a61d9b2c7305; nuovi campi inclusi in backup/ripristino.
- Risultati e limiti di verifica in docs/VERIFICA.txt.

# Versione 1.5.0

- Tema scuro ad alto contrasto; finestre persistenti al clic esterno, conferma su X/Esci/Esc e blocco della chiusura durante il salvataggio.
- Galleria fino a 10 foto, disponibile già nella creazione prodotto; caricamenti temporanei privati, collegamento atomico e scelta della foto principale.
- Prezzi pubblico/rivenditore e fino a 20 soglie quantità per listino/variante; calcolo server, selettori al banco e negli ordini/preventivi, regole storiche e prezzi manuali conservati. CSV e catalogo PDF aggiornati.
- Modifica degli ordini anche consegnati: conguaglio esplicito, stock per differenza e rettifiche ricavi con snapshot immutabili. Rimozione logica anche di ordini pagati/consegnati con rimborso, stock e storico coerenti; restrizioni operatori conservate.
- Metodo e importo pagamento fornitore nel nuovo carico; pagamento facoltativo alla conferma nella stessa transazione, riepilogo pagato/saldo e collegamento alle uscite.
- Migrazione a61d9b2c7305, successiva a f47c9a1d6208; conserva foto e importi precedenti e recupera gli eventi dei ricavi storici.
- Verifiche automatiche e limiti della consegna in docs/VERIFICA.txt.

# Versione 1.4.0

- Caricamento, sostituzione e rimozione foto prodotto; validazione, miniature, orientamento EXIF, formati JPG/PNG/WebP e salvataggio nel database.
- Catalogo prodotti PDF A4 con foto, varianti, prezzi facoltativi, categoria/ricerca e logo.
- Logo configurabile su documenti A4/80 mm, catalogo, etichette e report cassa; incluso nei backup.
- Prossimi ordini spostati in alto nella Panoramica; consegne senza data in fondo.
- Entrate e uscite con grafico, filtri, ricerca, paginazione e CSV; periodi oggi/mensile/scorso mese/data/intervallo anche per vendite e margini.
- Costi dei carichi distinti dai pagamenti; pagamenti parziali ai fornitori con revisioni, cassa, controllo contante e idempotenza.
- Migrazione f47c9a1d6208; recupero conferme storiche dei carichi senza creare pagamenti.
- 102 test backend, 24 controlli frontend e build TypeScript/React. Dettaglio e limiti in docs/VERIFICA.txt.

# Versione 1.3.0

- Sei caselle prodotto persistenti e modificabili in alto nella Vendita al banco, condivise tra postazioni.
- Account Operatore, assegnazioni multiple degli ordini e accesso dedicato /operatori con controlli di proprietà lato server.
- Creazione, modifica, avanzamento e rimozione logica degli ordini assegnati; audit, revisioni, vincoli su acconti, saldi e stock.
- Scadenze con completamento/riapertura, filtri e riepilogo dei prossimi sette giorni in dashboard.
- Note rapide personali, modificabili e persistenti, con scorciatoia Ctrl+Invio.
- Migrazione e83f4b19c507 e backup/ripristino delle nuove tabelle; conservazione dei dati esistenti.
- Verifiche: 86 test backend e 19 controlli frontend, build TypeScript/React; limiti in docs/VERIFICA.txt.

# Versione 1.2.0

- Codice articolo prima del nome; unicità globale senza distinzione tra maiuscole/minuscole, compresi CSV e assegnazione automatica.
- Categorie e sottocategorie da elenchi con pulsanti +; recupero delle voci esistenti senza cambiare gli snapshot storici.
- Matrice taglie × colori con quantità e pallini, affiancata da tabella modificabile di codici, prezzi, costi, barcode e scorte.
- Salvataggio atomico e idempotente, controlli sui permessi, revisioni del catalogo e giacenze concorrenti; scambio sicuro dei codici.
- Migrazione d24a6c8e9102: registro categorie e chiave univoca SKU; eventuali vecchi duplicati distinti con suffisso e audit.
- CSV con sottocategoria opzionale e compatibilità con le versioni precedenti.
- 68 test backend e 14 controlli frontend; build TypeScript/React. Limiti del collaudo in docs/VERIFICA.txt.

# Versione 1.1.0

- Fasce adulto XS–XXXXL, bambino da 1 a 14 anni e Taglia unica.
- Colori con pallino, 18 tinte predefinite e selettore della tinta personalizzata.
- Generatore taglia × colore con anteprima, codici univoci, idempotenza e salto delle combinazioni esistenti.
- Pallini nel catalogo, magazzino, banco vendita, documenti a video e PDF.
- Snapshot della tinta, import/export CSV compatibile con i CSV 1.0 e migrazione dei dati esistenti.
- Aggiorna-Windows.cmd con copia preventiva e ripristino in caso di errore; database vuoto separato dai dati operativi nello ZIP.

# Versione 1.0.0

Prima release modulare: autenticazione e permessi, catalogo/varianti, magazzini e storico, vendite al banco, ordini/acconti, arrivi, preventivi, cassa, statistiche, PDF interni, CSV nativo, backup e ripristino SQLite, script di installazione e avvio Windows.

Database iniziale vuoto con migrazione `950d4846a50a`. Tutti i dati operativi vengono inseriti dal titolare; i dati di test sono isolati. Consultare `docs/FUNZIONI_E_TEST.md` per le funzioni rinviate. Nessuna integrazione fiscale o Flazio dichiarata operativa.
