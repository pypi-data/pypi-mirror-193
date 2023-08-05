class Error(Exception):
    '''
    Base class for all controlled exceptions raised by the CDK.

    If possible, please do not raise this exception. Instead, choose one of its
    descendants. If none of the existing ones has a meaningful name for a new
    error condition that has to be accounted for, better create it.

    When used as context managers, connectors capture any other possible errors,
    and wrap them as bare Error exceptions with the original one as their cause.
    '''

class UnknownConnectorError(Error):
    '''
    Raised by `connector_for()` if it gets passed an unknown connector name.
    '''
    def __init__(self, name):
        super().__init__(f'Unknown connector name {name}')

class UnsupportedFormatError(Error):
    '''
    Raised by connectors, by contract, if they are asked to export to a format
    they do not support.
    '''
    def __init__(self, fmt):
        super().__init__(f'Unsupported format {fmt}')

class MissingConfiguration(Error):
    '''
    Raised by config.get() when a required environment variable is unset.
    '''
    def __init__(self, name):
        super().__init__(f'{name} is required')

class JobError(Error):
    '''
    Raised by the Tinybird client when a job it is waiting for has `error`
    status.
    '''

class RateLimitedForTooLongError(Error):
    '''
    Raised by the Tinybird client if it accumulates one hour of consecutive
    waits for the same rate-limited request.
    '''
    def __init__(self, max_rate_limit_retry_s):
        super().__init__(f'Rate-limited retries exceeded {max_rate_limit_retry_s} seconds')

class HTTPError(Error):
    '''
    Raised by the Tinybird client performs an unsuccessful request that is not
    retried.
    '''
    def __init__(self, method, response, error_message):
        status_code = response.status_code
        url = response.url
        super().__init__(f'{status_code} code for {method} {url}: {error_message}')

class UnsupportedCloudServiceSchemeError(Error):
    '''
    Raised by cloud URL parsing if given the URL of an unknown provider.
    '''
    def __init__(self, scheme):
        super().__init__(f'The cloud service scheme {scheme} is unsupported')

class UnsupportedCloudServiceError(Error):
    '''
    Raised by `client_for()` if it gets passed the name of an unsupported cloud
    provider.
    '''
    def __init__(self, service):
        super().__init__(f'The cloud service {service} is unsupported')
