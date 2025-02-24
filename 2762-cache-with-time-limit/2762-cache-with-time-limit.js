class TimeLimitedCache {
    constructor() {
        this.cache = new Map(); // Stores keys with values and expiration time
    }

    /**
     * @param {number} key
     * @param {number} value
     * @param {number} duration time until expiration in ms
     * @return {boolean} if an un-expired key already existed
     */
    set(key, value, duration) {
        let exists = this.cache.has(key);
        
        if (exists) {
            clearTimeout(this.cache.get(key).timeoutId); // Clear previous timeout
        }
        
        let timeoutId = setTimeout(() => {
            this.cache.delete(key);
        }, duration);
        
        this.cache.set(key, { value, timeoutId });

        return exists;
    }

    /**
     * @param {number} key
     * @return {number} value associated with key or -1 if expired
     */
    get(key) {
        return this.cache.has(key) ? this.cache.get(key).value : -1;
    }

    /**
     * @return {number} count of unexpired keys
     */
    count() {
        return this.cache.size;
    }
}
