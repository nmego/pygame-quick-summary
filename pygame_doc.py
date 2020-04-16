"""
ctrl+k, ctrl+2 will fold everything
except for block caret is currently in
"""
class pygame.camera:
    """
    Pygame currently supports only Linux and v4l2 cameras
    EXPERIMENTAL!
    """
    pass
class pygame.joystick:
    """Who cares?"""
    pass
class pygame.midi:
    """WHo careS?"""
    pass
class pygame.Overlay:
    """ Too complicated display
    """

class pygame.cdrom:
    __doc__:
        """
        This module, manages CD and DVD drives on a computer
        Can also control playback of audio CDs
        Must be initialized first

        Each CD object represents a cdrom drive
            Must also be initalized individually before it can do most things
        """
    cdrom.init() -> None
        """
        Initalize cdrom module. Happen automatically on pygame.init()
        Scan system for all CD devices   

        Safe to be called more than once
        """
    cdrom.get_init() -> bool
    cdrom.quit() -> None  
    cdrom.get_count(): -> count
        """
        When creating CD objects, you need to pass
        an integer id that must be lower than this count
        count will be 0 if no drives on the system
        """

    class CD:   
        __doc__:
            """
            Can create CD for each cdrom on system
            id argument is an integer of the drive starting at 0

            if CD object is not initialized, you can only  call
            CD.get_id() and CD.get_name()

            It is safe to create multiple CD objects for same drive
            """

        CD.init() -> None
            """
            Initialize the cdrom drive for use.

            May be a brief pause, avoid CD.init() 
            if program should not stop for a second or two
            """
        CD.get_init() -> None
        CD.quit()   

        CD.get_id() -> id
        CD.get_name() -> name
            """
            System name, for example: 
            E:\\
            """

        CD.get_busy() -> bool
            """
            If device is playing audio
            """
        CD.get_paused() -> bool
        CD.get_empty() -> bool
            """
            False if a cdrom is in the drive
            """
        CD.get_track_audio(track) -> bool
            """
            True if cdrom track has audio data
            """

        CD.get_current() -> track, seconds
        CD.get_numtracks() -> count
            """
            return 0 if empty or no tracks
            """
        CD.get_track_start(track) -> seconds
        CD.get_track_length(track) -> seconds

        CD.get_all() -> [(audio, start, end, length), ...]


        CD.play(track, start=None, end=None) -> None
            """
            Playback audio from an audio cdrom in the drive

            Track numbers start at zero
            """
        CD.stop() -> None
            """
            Stop audio playback

            does nothing if not playing audio
            """
        CD.pause() -> None   
        CD.resume() -> None

        CD.eject() -> None
            """
            Open cdrom drive and eject cdrom
            If playing or paused it will be stopped
            """

class pygame:
    __doc__:
        """ 
        The pygame package represents top-level package

        Most of top-level variable have been placed into pygame.locals
        This is meant to be used with "from pygame.locals import *"
        In addition to "Import pygame""

        All available pygame submodules are automatically imported
        Except for some optional ones, in which case pygame will provide
        a placeholder object to test for availability
        """

    pygame.init(): -> (numpass, numfall)
        """
        Initalize all imported pygame modules,
        return number of successful and failed inits

        You can always initalize individual modules manually,
        but pygame.init() is a convenient way to get all started

            init() for individual modules will raise exceptions if failed
            
            You may want to do so, to speed up program 
            or to not use modules your game does not require

        It is safe to call it more than once as repeated calls
        have no effect
        """
    pygame.get_init(): -> bool
        """Return true if pygame is currently initalized"""
        pass    
    
    pygame.quit(): -> None
        """
        Uninitalize all pygame modules that have been initialized

        When python interpreter shuts down, this method is called regardles
            So your program doesn't need it, unless it wants to
            terminate game resources and continue
        
        Safe to be called more than once as repeated calls have
        no effect
        """
    pygame.register_quit(callable) -> None
        """
        Register a function to be called when pygame quits

        Pygame modules do this automatically when initalizing
        So, this function will rarely be needed
        """      

    pygame.get_error(): -> errorstr
        """
        Get current error message

        SDL maintains an internal error message. Message
        will usually be given to you when pygame.error
        is raised, so rarely this function will be needed.
        """
    pygame.set_error(error_msg): -> None
        """See get_error"""
        pass
    raise pygame.error(message):
        """
        standard pygame exception

        Raised whenever:
        1. pygame operation fails
        2. SDL operation fails

        Derived from RuntimeError exception

        Always raised with a descriptive message
        Can catch any anticipated problems and deal with error
        """

    pygame.get_sdl_version() -> major, minor, patch
    pygame.get_sdl_byteorder() -> int
        """
        1234 --> little endian
        4321 --> big endian
        """

    pygame.encode_string([obj [, encoding [, errors [, etype]]]]) -> bytes or None
        """Encode a unicode or bytes object

        obj: Unicode --> encode
             bytes --> return unaltered
             else --> None
             not given --> Syntax Error
        
        encoding (string) --> encoding to use
            default is 'unicode_escape'

        errors (string) -> how to handle unencodable chars
            default is 'backslashreplace'

        etype (exception type) -> Exception type to raise for encoding error
            default is UnicodeEncodeErorr

        Primarily used for unit tests
        """
    pygame.encode_file_path([obj [, etype]]) -> bytes or None
        """
        Encode a Unicode or a bytes object as a file system path

        Encoding is the codec returned by
        sys.getfilesystemencoding()

        Primarly for unittests
        """
    
    class version:
        """
        Automatically imported with pygame package
        """
        pygame.version.ver = '1.2'
            # it can contain a micro release number too
            # e.g. '1.5.2'
        pygame.version.vernum = (1, 5, 3)     
            # tupled version
            # can easily be compared with similar formats
            # Example:
                if pygame.version.vernum < (1, 5):
                    print("Warning, older version")

            vernum.major = vernum[0]
            vernum.minor = vernum[1]
            vernum.patch = vernum[2]
        pygame.version.rev = 'a6f89747b551+'     
            # respository revision of the build
            # if ends with +, it contains uncommitted changes
            # Include it in bug reports, especially for non-release builds
class pygame.locals:
    """
    Contains various constants used by pygame, its contents are
    automatically placed on module namespac-e.

    However can include only pygame constants with a
    from pygame.locals import *

    examples:
    pygame.display FLAGS
    pygame.event EVENT TYPES
    pygame.key KEYBOARD CONSTANTS/MODS
    pygame.time TIMER_RESOLUTION
    """

class pygame.math:
    __doc__:
        """          
        Mainly Vector2 and Vector3

        Supporting:
            v+v, v-v, v*v (dot-product)
            n*v, v/n, v//n
            all are aelementwise

            if you want to multiply every element from vector v
            with every element from vector w, you can use 
            v.elementwise() * w

        coordinates of a vector can be retrieved or set using
        attributes or subscripts
        >>> v.x = 5
        >>> v[1] = 2 * v.x
        >>> v.z == v[2]

        Multiple coordinates can be set using slices or swizzling
        >>> v.xy = 1, 2
        >>> v[:] = 1, 2, 5

        requires Import
        """
    # All rad rotations are new in pygame 2.0.0  
    class Vector2:
        Vector2() -> Vector2
        Vector2(int) -> Vector2 # e.g. Vector2(4) == Vector2(4, 4)
        Vector2(float) -> Vector2
        Vector2(Vector2) -> Vector2
        Vector2(x, y) -> Vector2
        Vector2((x, y)) -> Vector2

        Vector2.as_polar() -> (r, phi)
        Vector2.from_polar((r, phi)) -> None

        Vector2.magnitude() -> float
        Vector2.magnitude_squared() -> float # Faster as avoids sqrt
        # there's also length() and length_squared() which do the exact same
        Vector2.normalize() -> Vector2 # same direction, length = 1
        Vector2.normalize_ip() -> None # normalize in place
        Vector2.is_normalized() -> bool
        Vector2.scale_to_length(float) -> None # Can scale to 0, if vector is 0 vector ZeroDivisonError


        Vector2.dot(Vector2) -> float
        Vector2.cross(Vector2) -> Vector2
        Vector2.reflect(Vector2) -> Vector2
        Vector2.reflect_ip(Vector2) -> None
        Vector2.distance_to(Vector2) -> float
        Vector2.distance_squared_to(Vector2) -> float
        Vector2.lerp(Vector2, float) -> Vector2 # 0=self, 1=other
        Vector2.slerp(Vector2, float) -> Vector2
            """
            Spherical interpolation

            second argument, often called t, must be in range [-1, 1]
            it paramaetrizes, where, in between two vectors, the result
            should be.

            if a negative value is given, interpolation will not take
            the complement of the shortest path
            """
        Vector2.angle_to(Vector2) -> float

        Vector2.rotate(angle) -> Vector2
        Vector2.rotate_rad(angle) -> Vector2
        Vector2.rotate_ip(angle) -> Vector2
        Vector2.rotate_ip_rad(angle) -> Vector2
    
        Vector2.elementwise() -> VectorElementwiseProxy
            """
            Apply following operation to each element of vector

            Ex.  v.elementwise() * w
            """

        Vector2.update() -> None
        Vector2.update(int) -> None
        Vector2.update(float) -> None
        Vector2.update(Vector2) -> None
        Vector2.update(x, y) -> None
        Vector2.update((x, y)) -> None
       
    class Vector3:
        Vector3() -> Vector3
        Vector3(int) -> Vector3
        Vector3(float) -> Vector3
        Vector3(Vector3) -> Vector3
        Vector3(x, y, z) -> Vector3
        Vector3((x, y, z)) -> Vector3

        Vector3.as_spherical() -> (r, theta, phi)
        Vector3.from_spherical((3, theta, phi)) -> None

        Vector3.magnitude() -> float
        Vector3.magnitude_squared() -> float
        Vector3.normalize() -> Vector3
        Vector3.normalize_ip() -> None
        Vector3.is_normalized() -> bool
        Vector3.scale_to_length(float) -> None


        Vector3.dot(Vector3) -> float
        Vector3.cross(Vector3) -> float
        Vector3.reflect(Vector3) -> Vector3
        Vector3.reflect_ip(Vector3) -> None
        Vector3.distance_to(Vector3) -> float
        Vector3.distance_squared_to(Vector3) -> float
        Vector3.lerp(Vector3, float) -> Vector3
        Vector3.slerp(Vector3, float) -> Vector3
        Vector3.angle_to(Vector3) -> float

        Vector3.rotate(Vector3, angle) -> Vector3 # around given axis
        Vector3.rotate_rad(Vector3, angle) -> Vector3
        Vector3.rotate_ip(Vector3, angle) -> None
        Vector3.rotate_ip_rad(Vector3, angle) -> None
        Vector3.rotate_x(angle) -> Vector3 # around x-axis
        Vector3.rotate_x_rad(angle) -> Vector3
        Vector3.rotate_x_ip(angle) -> None
        Vector3.rotate_x_ip_rad(angle) -> None
        # repeat for y and z


        Vector3.elementwise() -> VectorElementwiseProxy

        Vector3.update() -> None
        Vector3.update(int) -> None
        Vector3.update(float) -> None
        Vector3.update(Vector3) -> None
        Vector3.update(x, y, z) -> None
        Vector3.update((x, y, z)) -> None
class pygame.time:
    __doc__:
        """
        Time is in ms, most platforms have limited 
        time resolution of around 10 ms.
        This is given in the TIMER_RESOLUTION constant
        """

    time.get_ticks() -> ms
        """
        Since pygame.init() was called, before it is called it is 0
        """
    time.wait(ms) -> time 
        """
        Sleeps the process to share the process with other programs.
        Slightly less accurate than time.delay()
        Returns the actual number of milliseconds used.
        """
    time.delay(ms) -> time
        """
        Will actually use the process to make delay more accurate.
        """   
    time.set_timer(eventid, ms, once=False) -> None # once is pygame 2+
        """
        First event will not appear until the amount of time has passed

        It is best to use value between pygame.USEREVENT and pygame.NUMEVENTS
        """

    class Clock()
        Clock() -> Clock

        Clock.tick(framerate=0) -> ms
            """
            Should be called once per frame, will compute how many ms have
            passed since prev call.

            This function will delay to keep the game running slower than the
            given ticks per second if you pass framerate.

            Uses SDL_Delay which is not accurate on every platform, but does
            not use much CPU. Use tick_busy_loop if you want an
            accurate timer and don't mind chewing CPU
            """
        Clock.tick_busy_loop(framerate=0) -> ms # more accurate, more CPU
           

        Clock.get_time() -> ms # since prev call to Clock.tick
        Clock.get_raw_time() -> ms # doesn't include any time used while delaying in Clock.tick()

        Clock.get_fps() -> fps # Averaging last ten calls to Clock.tick()
        
class pygame.Color:
    __doc__:
        """
        Color(r, g, b) -> Color
        Color(r, g, b, a=255) -> Color
        Color(color_value) -> Color

        Allow +, -, *, //, %  and ~ (unary operation) to create new colors.
        Also equality comparison with other color objects and 3/4-element tuples
                        of integers

        Support conversions to other color spaces (HSV - HSL)

        Let you adjust single color channels

        Arithmetic operations and correct_gamme preserve subclasses
        For binary operators, class of returned color is left hand color object

        Color objects export the C level array interface
                    - a read-only one dimensional unsigned byte array of same
                        assigned length as the color
        For CPython 2.6 and later. New buffer interface is also exported
        
        // and % do not raise an exception for division by 0
        Color(255, 255, 255, 255) % Color(64, 64, 64, 0) == Color(63, 63, 63, 0)
        


        supported color_value formats:
            - Color object 
            - color name str e.g. 'red'
                all supported name strings (colordict module): 
                   https://github.com/pygame/pygame/blob/master/src_py/colordict.py
            - HTML color format str:
                '#rrggbbaa' or '#rrggbb'
                2-digit hex numbers in range of 0 to 0xFF inclusive
            - int value of color to use
                using hex numbers can make it more readable
                e.g. 0xrrggbbaa
            - tuple/list of int color values
        """
    Color.r -> int 
    Color.g -> int
    Color.b -> int
    Color.a -> int

    Color.cmy -> tuple
        """
        CMY represetnation
        C = [0, 1]
        M = [0, 1]
        Y = [0, 1]
        rounding errors

        Subtractive representation
        where C = 0, M = 0, K = 0 make black
        """
    Color.hsva -> tuple
        """
        HSVA representation
        H = [0, 360]
        S = [0, 100]
        V = [0, 100]
        A = [0, 100]

        may cause some rounding errors
        and not return the exact HSV vlues

        Hue --> pure color
        Value --> how bright it is
        Lightness --> how white it is

        hsva/hsla better for graphic designers
        """
    Color.hsla -> tuple
    Color.i1i2i3 -> tuple
        """
        I1 = [0, 1]
        I2 = [-0.5, 0.5]
        I3 = [-0.5, 0.5]
        """

    Color.set_length(len) -> None
        """
        Set number of elements in the Color to 1,2,3 or 4
        default is 4.
        useful if you want to unpack to r.g.b and not r.g.b.a
        """    
    Color.normalize() -> tuple
        """
        Return normalized RGBA values of the Color
        """

    Color.correct_gamma(gamma) -> Color    
        """
        Apply a certain gamma value to the color

        https://www.colormatters.com/the-power-of-gamma
        """
    Color.lerp(Color, float) -> Color
        """
        Return a linear interpolation to the given Color
        In RGBA space.

        float determines how far between self and other the result gonna be
        from 0 to 1
        0 --> self is returned
        1 --> other is returned 

        pygame 2.0.1+
        """
class pygame.event:
    __doc__:
        """
        Input queue is heavily dependent on pygame.display module.
        If display is not initalized and video mode not set, may not work properly

        Event subsystem should be called from main threads, if you want to post
        events into the queue from other threads use pygame.fastevent module.

        Event queue has an upper limit (128 for standard SDL 1.2).
        When full queue, new events are quietly dropped.
        So, your prorgam must regularly check for events and process them.
        To speed up queue processing, use pygame.event.set_blocked() to limit 
        which events get queued.

        To get state of various input devices, you can forego event queue and 
        access input devices directly with appropriate modules (pygame.mouse)
        If you use this method, remember that pygame requires some form
        of communication with system window mnager and other parts of platform.
            To keep pygame in sync with system, you nee to call 
            pygame.event.pump() to keep everything current (Usually once per loop)

        The queue contains pygame.event.EventType event objects.
        By default all event types can be placed on queue. But you can filter.

        All pygame.event.EventType contain:
            - Event type identifier
                - EventType.type
            - Attributes specific to that event type
                - EventType.__dict__ or directly as an attribute of event object
        - The  EventType has no method functions
        - Can create own events with pygame.event.Event()

        The identifier is in between the values of NOEVENT and NUMEVENTS
        User defined events should have a value in inclusive range of USEREVENT
        to NUMEVENTS - 1. It is recommended all user events follow this system.

        Events support equality and inequality comparions, are equal if same 
        type and same attribute.

        pygame.event.event_name() can be used to get a string representing name
        of event type.

            ---
            QUIT --> None
            ACTIVEEVENT -> gain, state #  window has gain/lost mouse/keyboard/visiblity focus

            KEYDOWN -> unicode, key, mod
            KEYUP -> key, mod
            
            MOUSEMOTION -> pos, rel, buttons
            MOUSEBUTTONUP -> pos, button
            MOUSEBUTTONDOWN -> pos, button
            
            JOYAXISMOTION -> joy, axis, value
            JOYBALLMOTION -> joy, ball, rel
            JOYHATMOTION -> jay, hat, value
            JOYBUTTONUP -> joy, button
            JOYBUTTONDOWN -> joy, button
            
            VIDEORESIZE -> size, w, h
            VIDEOEXPOSE -> none # Hardware displays that draw direct to screen
            USEREVENT -> code

            With SDL2:
            AUDIODEVICEADDED -> which, iscapture
            AUDIODEVICEREMOVED -> which, iscapture
            FINGERMOTION -> touch_id, finger_id, x, y, dx, dy
            FINGERDOWN -> touch_id, finger_id, x, y, dx, dy
            FINGERUP -> touch_id, finger_id, x, y, dx, dy
            MULTIGESTURE -> touch_id, x, y, pinched, rotated, num_fingers

            TEXTEDITING -> text, start, length
            TEXTINPUT -> text

            In pygame2.0:
            (Can recognize text or files dropped in its window)
            DROPBEGIN
            DROPCOMPLETE
            DROPFILE -> file (its path)
            DROPTEXT -> text (only supported on X11)
            ---

        """

    event.pos(Event) -> None
        """
        Especially used for placing pygame.USEREVENT on the queue
        (at end of queue)
        Although any type of event can be placed.
        If using system event types, you should be sure to
        create standard attributes with appropriate values.
        """
    event.pump() -> None
        """
        Internally proces pygame event handlers

        For each frame of your game, you will need to make some sort of call to 
        the queue, to ensuer your program can internally interact with OS.
        If you are not using other event functions in your game, you should 
        call pygame.event.dump() to allow pygame to handle internal actions

        Not necessary if program consistently processing events on the queue
        through other pygame.event functions

        There are important things that must be dealt with internally.
        The main window may need to be repainted or respond to system. If you
        fail to make a call to the event.queue for too long, system may decide
        program is locked up.

        SHOULD ONLY BE CALLED IN THE THREAT THAT INITIALIZED PYGAME.DISPLAY
        """

    event.get(eventtype=None, pump=True) -> Eventlist
        """
        Get all events from the queue
        (Also remove them from the queue)

        If a type or sequence of types is given, only those messages will
        be removed.
        (Careful because queue could eventually fill up then)

        If pump is True, then pygame.event.pump() will be called
        """
    event.poll() -> EventType instance
        """
        Returns a single event from queue. If empty a pygame.NOEVENT is
        returned, returned event is removed from queue.

        SHOULD ONLY BE CALLED IN THE THREAD INITALIZED PYGAME.DISPLAY
        """
    event.wait() -> EventType instance
        """
        Exactly same as poll, except if queue is empty, wait until
        one is created. While it is waiting, the program will sleep in an idle 
        state. This is important for programs that want to share system
        with other applications.
        """

    event.peek(eventtype=None, pump=True) -> bool
    event.clear(eventtype=None, pump=True) -> None

    event.set_blocked(eventtype) -> None
        """
        If None --> block all
        can pass a type or a typelist
        """
    event.set_allowed(eventtype) -> None
        """
        If None --> Allow all
        """    
    event.get_blocked(type) -> bool

    event.set_grab(bool) -> None
        """
        When program runs windowed, it will share mouse and keyboard
        devices with other applications that have focus, if event_grab = True
        it will lock all input into your prorgam.

        It is best to not always grab the input, since it prevents user 
        from doing other things on their system.
        """
    event.get_grab() -> bool    

    event.event_name(type) -> string
    event.custom_type() -> int
        """
        Reserves a pygame.USEREVENT for a custom use
        If too many events are made, a pygame.error is raised
        """

    class EventType:
        EventType.type -> int #(Read-only)
        EventType.__dict__ -> dict #(Read-only)

class pygame.mixer:
    __doc__:
        """
        loading sound objects and controlling payback.
        optional depends on SDL_MIXER, should test that mixer
        is available and initialized before using it.

        It has a limited number of channels for playback, usually
        programs tell pygame to start playing audio and it selects
        an avalable channel automatically. The default is 8 simultaneous
        channels, but complex programs can get more precise control
        over number of channels and their use.

        All sound playback is mixedi n background threads. When you begin
        to play a Sound object it will return immediately while the sound continues
        to play.

        mixer also has a special streaming channel, for music playback through
        mixer.music

        Must be initialized like other pygame modules, but its init takes
        several optional arguments to control playback rate and sample size
        Pygame will default to reasonable values, but pygame cannot perform
        sound resampling, so the mixer should be initialized to match values
        of audio resources.

        NOTE: for less laggy sound use a smaller buffer size. You can change
        default buffer by calling mixer.pre_init() before mixer.
        init() or pygame.init() is called
        """

    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512,
                          devicename=None) -> None
        """
        preset mixir init arguments.

        Main reason for this, is you cannot pass any arguments to pygame.init()
        note: in pygame 2.0.0 buffersize changed from 4096 to 512
        and feq from 44100 to 22050
        """
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCE_CHANGE | AUDIO ALLOW_CHANNELS_CHANGE) -> None
        """
        size --> how many bits are used for each audio sample
                 -ve --> signed sample values would be used
                 +ve --> unsigned
            In pygame 2.0.0: size can be 32 bit.
        
        channels -> 1 for mono, 2 for stereo.
            In pygame 2.0.0: number of channels can be 4 or 6

        buffer -> number of internal samples used in the sound mixer,
                default values should work for most cases. but it can be lowered
                to reduce latency, but sound dropout may occur. it can be raised
                to ensure playback never skips, but it will impose latency.
                MUST BE A POWER OF 2 (else rounded to next nearest power of 2
        
        Some platforms require this module to be initialized after display modules
        have initialized, pygame.init() takes care of that but cannot pass
        any arguments.

        When using allowedchanges = 0, it will convert the samples at runtime
        to match what the hardware supports. for example, a soundcard may not
        support 16bit sound samples, so it will use 8bit samples internally.
        if AUDIO_ALLOW_FORMAT_CHANGE is enabled, then requested format will 
        change to the closest that SDL supports.
        There's Also
            AUDIO_ALLOW_FREQUENCY_CHANGE
            AUDIO_ALLOW_FORMAT_CHANGE
            AUDIO_ALLOW_CHANNELS_CHANGE
            AUDIO_ALLOW_ANY_CHANGE
        """
    mixer.get_init() -> (frequency, format, channels)
    mixer.quit() -> None

    mixer.stop() -> None # stop playback of all active channels
    mixer.pause() -> None
    mixer.unpause() -> None
    mixer.fadeout(time) -> None # fadout volume before stopping, time in ms

    mixer.set_num_channels(count) -> None
    mixer.get_num_channels() -> count
    mixer.set_reserved(count) -> None
        """
        reserve any number of channels that will not be automatically
        selected for playback by sounds, if sounds are currently playing
        on reserved channels, they will not be stopped.

        This allows the application to rserve a specific number of
        channels for important channels that must not be dropped or 
        have a guaranteed channel to play on.
        """
    mixer.find_channel(force=False) -> channel
        """
        return an inactive channel object
        If there are no inactive Channels this returns None
        but if so, and force=True, find channel with longest
        running sound and return it.

        if mixer.set_reserved() those channels will not
        be returned here
        """

    mixer.get_busy() -> bool # test if any sound is being mixed

    mixer.get_sdl_mixer_version(linked=True) -> (major, minor, patch)

    class Sound:
        Sound(filename) -> Sound
        Sound(file=filename) -> Sound
        Sound(buffer) -> Sound
        Sound(buffer=buffer) -> Sound
        Sound(object) -> Sound
        Sound(file=object) -> Sound
        Sound(Array=object) -> Sound
            """
            Create a new Sound object from a filename/python file
            object/ readable buffer object.

            Limited resampling will be performed to help the
            sample match the init arguments for the mixer.

            A bytes object can be either a pathname or a buffer object.
            Use file or buffer keywords to avoid ambiguity.

            If the array keyword is used, the object is expected to 
            export a new buffer interface.


            The sound object represents actual sound sample data.
            Methods that change state of Sound object will the all
            instances of the Sound playback.

            Sound can be loaded from an OGG audio file or from an uncompressed
            WAV

            Note: The buffer will be copied internally, no data will be shared
            between it and the Sound object.

            For now buffer and array support is consistent with sndarray.make_sound
            for Numeric arrays, in that sample sign and byte order are ignored.
            THis will change, either by correctly handling sign and bye order,
            or by raising an exception when different, also source samples are
            truncated to fit audio sample size.
            """

        Sound.play(loops=0, maxtime=0, fade_ms=0) -> Channel
            """
            This will forcibly select a channel, so may cut off
            a currently playing sound if necessary

            loops == -1 --> indefinitely looping.

            face_ms --> make sound start playing at 0 volume
            then face up to full volume over time given.
            """
        Sound.stop() -> None
        Sound.fadeout(time) -> None  

        Sound.set_volume(value) -> None # 0.0 to 1.0
        Sound.get_volume() -> value

        Sound.get_num_channels() -> count
        Sound.get_length() -> seconds
        Sound.get_raw() -> bytes
    class Channel:
        Channel(id) -> Channel
            """
            Return a Channel object for one of the current channels.

            The id must be a value from 0 to value of pygame.mixer.get_num_channels()

            Can be used to get fine control over playback of Sounds.
            Pygame manages them by default, so using channels is entirely optional.
            """

        Channel.play(Sound, loops=0, maxtime=0, face_ms=0) -> None    
        Channel.stop() -> None
        Channel.pause() -> None
        Channel.unpause() -> None
        Channel.fadeout(time) -> None

        Channel.set_volume(value) -> None
        Channel.set_volume(left, right) -> None
            """
            If stereo mode, and second argument is None, 
            first argument would be volume of both speakers

            example:

            >>> sound = pygame.mixer.Sound("s.wave")
            >>> channel = s.play() # Sound plays at full volume
            >>> sound.set_volume(0.9) # 0.9 of full volume
            >>> sound.set_volume(0.6) # 0.6
            >>> channel.set_volume(0.5) # 0.3 (0.6 x 0.5)
            """
        Channel.get_volume() -> value # doesn't take into account sound.set_volume
        Channel.get_busy() -> bool
        Channel.get_sound() -> sound

        Channel.queue(Sound) -> None # only one queued at a time
        Channel.get_queue() -> Sound

        Channel.set_endevent() -> None
        Channel.set_endevent(type) -> None # Every time a sound finishes playing
            """
            Note, 
            if looped, end event is sent only once after being played
            loops + 1 times.

            IF Channel.stop() or Channel.play() is called. event will be posted
            immediately.

            type argument will be event id sent to thequeue. A good choice
            would be a value between pygame.locals.USEREVENT and pygame.locals.NUMEVENTS
            """
        Channel.get_endevent() -> type # No endevent --> pygame.NOEVENT
                
    class music:
        __doc__:
            """
            Difference is, music is streamed and never actually loaded all at once.

            Mixer system supports a single music stream at once.
            MP3 is limited, On somem systems an unspported format can crach
            the program. e.g. Debian Linux, consider using OGG instead.
            """

        music.load(filename) -> None
        music.load(object) -> None # file object
            """
            If a music stream is already playing, it will be stopped
            This does not start the music playing
            """    
        music.unload() -> None # To free resources, new in 2.0.0

        music.play(loops=0, start=0.0) -> None
        music.rewind() -> None
        music.stop() -> None
        music.pause() -> None
        music.unpause() -> None
        music.fadeout(time) -> None

        music.set_volume(value) -> None
        music.get_volume() -> value()
        music.get_busy() -> bool
        music.set_pos(pos) -> None
            """
            pos, a float (or a number converted to a float.)
            depends on music format.

            MOD: integer pattern number in the module
            OGG: absolute position in seconds, from beginning
            MP3: relative position in seconds, from current position

            For absolute positioning in an MP3 file, first call rewind()

            other fire formats are unsupported.

            Newer versions have better support than earlier.

            This function, calls underlining SDL_mixer function
            Mix_SetMusicPosition
            """
        music.get_pos() -> time
            """
            number of ms that the music has been playing for
            does not take into account any starting position offsets
            """
        music.queue(filename) -> None                
            """
            If current sound is ever stopped or changed,
            queued sound will be lost.

            Only queue happens once current sounds n aturally stops
            """

        music.set_endevent() -> None
        music.set_endevent(type) -> None    
            """
            Event will be queued every time the music finishes,
            not just the first time, to stop event from being queued
            call this method with no argument
            """
        music.get_endevent() -> type


class pygame.font:
    __doc__:
        """
        Rendering TrueType fonts into a new Surface object.
        Accepts any UCS-2 character ('u0001' to 'uFFFF'). 
        
        This module is optional and requires SDL_ttf as a dependency
        You should test that pygame.font is available and initialized before
        attempting to use the module.
        
        Pygame comes with a default font builtin, can always be accessed by passing 
        None.

        Most of the work done with fonts are done by using the actual Font objects.

        To use the pygame.freetype based pygame.ftfont as pygame.font
        define environment variable PYGAME_FREETYPE before first import
        of pygame. 

        Module pygame.ftfont is a pygame.font compatible module that
        pases all but one of font module unit tests. IT does not have the 
        UCS-2 limitation of the SDL_ttf based font module. so fails to raise an 
        exception for a code point greater than 'uFFFF'. if pygame.freetype is
        unavailable. SDL_ttf font module will be loaded instead.
        """

    font.init()
    font.get_init()
    font.quit()

    font.get_default_font() -> string 
        """
        filename of system font, not full path, can be found in same directory.
        """
    font.get_fonts() -> list of strings 
        """
        get list of all fonts available on system.
        names of fonts iwll be lowercase with all space and punctation removed.

        works on most systems. but some will return an empty list.
        """
    font.match_font(name, bold=False, italic=False) -> path
        """
        Returns the full path to a font file on system.
    
        The font name can actually be a comma separated list of font names to try
        """       

    font.SysFont(name, size, bold=False, italic=False) -> font
        """
        Create a Font object from system fonts.

        If a suitable system font is not found,
        fall back on loading default pygame font.

        name can be comma separated list of font names
        """

    class Font:
        Font(filename, size) -> Font
        Font(object, size) -> Font # object is a file object
            """
            size is height of font in pixels.

            If filename is None, default font will be loaded.
            If a font cannot be loaded from arguments --> exception
            Once created, size cannot be changed.

            Font objects are mainly used to render text into new Surface objects.

            render can emulate bold or italic, but it is better to load from an
            actual italic or bold glyphs.

            Can be regular strings or unicode.
            """

        Font.render(text, antialias, color, background=None) -> Surface
            """
            Text can only be a single line. 
                newline characters are not rendered.
                Null characters (x00) raise a typeError
                both Unicode and char (byte) strings are accepted.
                    For unicode strings only UCS-2 characters ('u0001' to 'uFFFF') 
                    are recognized, any greater --> UnicodeError

                    For char strings, a LATIN1 encoding is assumed
            
            antialias is a boolean.

            color argument is color of text.
            optional background is a color to use for text background (else transparent)

            Surface returned will be of dimensions required to hold the text.
            (Same as those returned by Font.size()). If an empty string is passed,
            a blank surface will be returned, 1px-wide and height of font.

            If AA is not used: returned image will always be 8-bit with two-color palette.
                If background is transparent --> a colorkey will be set
            AA images are rendered to 24-bit RGB images.
                If transparent, a pixel alpha will be included.
            
            Optimization:
                If you know final destination will always have a solid background.
                And text is AA, you can improve performance specifying background color.

                So image will maintain transparency information by colorkey rather than
                less efficient alpha values.

           ONLY A SINGLE THREAD CAN RENDER TEXT AT ANY TIME.
           """     

        Font.size(text) -> (width, height)

        Font.set_underline(bool) -> None
            """
            When enabled, all rendered fonts will include a 1pixel underline.
            """
        Font.get_underline() -> bool    
        Font.set_bold(bool) -> None # different wdith from normal.
        Font.get_bold() -> bool
        Font.set_italic(bool) -> None # different width from normal.
        Font.get_italic() -> bool

        Font.metrics(text) -> list
            """
            Gets metrics for each character in passed string

            List contains tuple for each character containing
                minimum x offset, maximum x offset, min y offset, max y offset,
                advance offset (bearing plus width) of character.

                None is entered for each unrecognized character.
            """
        Font.get_linesize() -> int
            """
            Return height in pixels for a line of text with the font.
            When rendering multiple lines, this is the recommended amount of space.
            """
        Font.get_height() -> int
            """
            Height in pixels of the actual rendered text
            Average size for each gylph in the font
            """  
        Font.get_ascent() -> int
            """
            Return height in pixels for font ascent.
            ascent is number of pixels from font baseline to top of font.
            """
        Font.get_descent() -> int         
class pygame.freetype:
    __doc__:
        """
        replacement for pygame.font, has all the functionality of original
        + many new features. yet has absolutely 0 dependencies on SDL_ttf. 
        It is implemented directly on Freetype 2. 

        All font file formats supported by FreeType can be rendered, namely
        TTF, Type1, CCF, OpenType, SFNT, PCF, FNT, BDF, PFR and Type42 fonts
        All glyphs having UTF-32 code points are accessible.

        Moost work on fonts is done using Font instances, Module itself
        only has routines for initialization and creation of Font objects.

        Extra support of bitmap fonts is available.
        Available bitmap sizes can be listed (Font.get_sizes()) 
        For bitmap only fonts, Font can set the size for you (Font.size property)

        For now undefined character codes are replaced with .notdef character.

        Pygame comes with a built-in default font, by passing None to Font constructor

        This module must be imported explicitly
        >>> import pygame
        >>> import pygame.freetype
        """

    freetype.get_error() -> str
        """
        Return a description of last error occured in the FreeType2 library
        or None if no errors have occurred.
        """
    freetype.get_version() -> (int, int, int)

    freetype.init(cache_size=64, resolution=72)
        """
        Initialize the underlyting FreeType library.
        pygame.init() will automatically call this if module is imported

        default cache_size --> maximum number of glyphs cached at any time by module
            Exceedingly small values will be automatically tuned for performance

        default pixel resolutions in dots per inch can be given to adjust font scaling.
        """
    freetype.get_init() -> bool
    freetype.quit()

    freetype.get_cache_size() -> long
    freetype.get_default_resolution() -> long
    freetype.set_default_resolution([resolution])
        """
        If omitted or zero,
        set to 72 DPI
        """

    freetype.SysFont(name, size, bold=False, italic=False) -> Font
    freetype.get_default_font() -> string

    class Font:
        Font(file, size=0, font_index=0, resolution=0, ucs4=False) -> Font
            """
            file is a string for filename ora file-like object or None

            size --> default size in points --> size of rendered characters.
                Because of way caching system works, default size on the constructor
                doesn't imply a performance gain over manually passing the size
                on each function call.

            font_index --> if font file has more than one font

            resolution --> sets pixel size for DPI. if 0 then efault module value 
                set by init() is used

            ucs4 argument --> sets default translation mode:
                0 --> Recognize UTF-16 surrogate pairs 
                1 --> To treat Unicode text as UCS-4 with no surrogate pairs.
            """
        
        Font.name -> string #Readonly
        Font.path -> unicode #Readonly
        Font.resolution -> int #Readonly

        Font.size -> float   
        Font.size -> (float, float)
            """
            Can be a single point size
            or a font ppem (widtht, height) tuple.
            Size values are non-negative.
            0 size or width represents an undefined size.

            For a scalable font, a single number value is
            equivalent to a tuple with width = height.
            
            For embedded bitmaps, as listed by get_sizes() use
            nominal width and height to select an available size.

            Font size differs for non-scalable, bitmap font.
            During a method call it must match one of
            the availalbe sizes returned by method get_sizes()
            If not, an exception is raised. If size is a single number.
            The size is first matched against point size match.
            If no match, the n available size with same nominal width and
            height is chosen.
            """
        Font.height -> int
            """
            READ ONLY

            Gets height of font, average value of all glyphs in the font
            """
        Font.ascender -> int # unscaled in font units
        Font.descender -> int # unscaled in font units

        Font.get_sized_ascender(<size>=0) -> int # scaled
        Font.get_sized_descender(<size>=0) -> int # scaled
        Font.get_sized_height(<size>=0) -> int
        Font.get_sized_glyph_height(<size>=0) -> int # Scaled bounding box height in pixels
        Font.get_sizes() -> [(int, int, int, float, float), ...]
            """
            Return a list of tuple records,
            one for each point size supported, each containing

            point size, height in pixels, width in pixels,
            horizontal ppem in fractional pixels,
            vertical ppem in fractional pixels
            """
        Font.get_metrics(text, size=0) -> [(...), ...]
            """
            (min_x, max_x, min_y, max_y, horizontal_advance_x, horizontal_advance_y)
            the min/max values are returned as grid-fitting pixel
            coordinates of type int (bounding box)

            advance values are float values.

            Metrics are adjusted for current rotation, strong and
            oblique settings.

            if text is a char (byte) string then assumed to be LATIN1

            """


        Font.get_rect(text, style=STYLE_DEFAULT, rotation=0, size=0) -> rect
            """
            Get final dimensions and origin in pixels of text using
            the optional size in points, style and rotation. for other 
            relevant render properties (and any optional arguments). default
            values set for Font instance are used.

            Return a Rect containing width and height of text's bounding box
            and position of text's origin. Origin is useful for aligning separately 
            rendered pieces of text. It gives baseline position and bearing at
            start of text.

            if text is a char (byte) string it is assumed to be LATIN1

            Optionally can be None, which will return the bounding rectangle for
            the text passed to a previous:
            get_rect(), render(), render_to(), render_raw() or render_raw_to()
            """
        Font.render(text, fgcolor=None, bgcolor=None, style=STYLE_DEFAULT,
                        rotation=0, size=0) -> (Surface, Rect)
             """
            Return a new surface with text rendered to it in color given by fgcolor
            if None fgcolor. default fgcolor is used.

            if bgcolor is given, surface will be filled, else transparent, 0 alpha
            Normally returned surface has a 32bit pixel size. However if 
            bgcolor is None and AA is disabled. a monochrome 8bit colorkey surface
            with colorkey set for background color is returned.

            text can be None, which will render the text passed to a previous
            render function (or get_rect)
            """
        Font.render_to(surf, dest, text, fgcolor=None, bgcolor=None, 
            style=STYLE_DEFAULT, rotation=0, size=0) -> Rect
            """
            Render string text to the pygame.Surface surf
            at position dest, a (x, y) surface coordinate pair.
            if either x or y is not an integer it is converted to one if possible.
            A rect instance is acceptable as dest.

            If a bgcolor is given, text bounding box is first filled with
            that color. then text is blitted next. Both background fil and 
            text rendering involve full alpha blits (all alpha values affect blit) 

            text can be set to None too!
            Example of using that:"""
                def word_wrap(surf, text, font, color=(0, 0, 0)):
                    font.origin = True
                    words = text.split(' ')
                    width, height = surf.get_size()
                    line_spacing = font.get_sized_height() + 2
                    x, y = 0, line_spacing
                    space = font.get_rect(' ')
                    for word in words:
                        bounds = font.get_rect(word)
                        if x + bounds.width + bounds.x >= width:
                            x, y = 0, y + line_spacing
                        if x + bounds.width + bounds.x >= width:
                            raise ValueError('word too wide for surface') 
                        if y + bounds.height - bounds.y >= height:
                            raise ValueError('text too long for surface')
                        font.render_to(surface, (x, y), None, color)
                        x += bounds.width + space.width
                     return x, y              

            """
            When render_to is called with same font_properties as get_rect

            render_to will use the same layout calculated by get_rect, else
            recalculate thelayout if called with a text string, or a property has
            changed.

            of course, if text is char (byte) it is assumed to be LATIN1
            """
        Font.render_raw(text, style=STYLE_DEFAULT, rotation=0, size=0, invert=False)
            -> (bytes, (int, int))
            """
            Like render() but with pixels returned as a bye string of 
            8-bit gray-scale values. foregound color is 255, background 0.
            Useful as an alpha mask for a foreground pattern.
            """
        Font.render_raw_to(array, text, dest=None, style=STYLE_DEFAULT, rotation=0,
                           size=0, invert=False) -> (int, int)
            """
            Render to an array object exposing an array struct interface. 
            Must be two dimensional with integer items. default dest value,
            None is equivalent to position (0, 0).

            As with other render methods, text can be None
            """

        Font.style -> int
            """
            Gets or sets default style of Font
            will be used for all text rendering and size calculations

            style values may be a bitwise OR | of one or more of foll. constants
                STYLE_NORMAL
                STYLE_UNDERLINE
                STYLE_OBLIQUE
                STYLE_STRONG
                STYLE_WIDE
                STYLE_DEFAULT

            can be found on FreeType constants module

            STYLE_OBLIQUE and STYLE_STRONG are for scalable fonts only
            AttributeError for bitmap font, or RuntimeError for inactive font
    
            Assigning STYLE_DEFAULT to style property leaves it unchanged
            """
        Font.underline -> bool
        Font.strong -> bool
        Font.oblique -> bool
        Font.wide -> bool # stretched horizontally when drawing text similar to font.Font bold
        Font.use_bitmap_strikes -> bool
            """
            Some scalable fonts include embedded bitmaps for particulat point sizes.

            This propety controls whether they are used or not.

            If True, the default, to permit bitmap strikes for a non-rotated render
            wither no style other than wide or underline
            """
        Font.antialiasd -> bool
        Font.kerning -> bool
        Font.vertical -> bool
        Font.pad -> bool
            """
            If true: text boundary rectangle will be inflated
            to match that of font.Font, otherwise, boundary
            rectangle is just large enough for the text
            """
        Font.origin -> bool
            """
            If True, render_to_ and render_raw_to()
            will take the dest position to be that of text
            origin as opposed to be top-left corner of bounding box
            """    
        Font.ucs4 -> bool:
            """
            By default freetype module performs UTF-16 surrogate pair
            decoding, this allows 32-bit escape sequences ('Uxxxxxxxx')
            between 0x10000 and 0x10FFFFF to represent that corresponding 
            UTF-32 code points on Python interpreters built with a UCS-2 
            Unicode type (on windows for instance)

            It also maens character values within UTF-16 surrogate area
            (0xD800 to 0xDFFF) are considered part of a surrogate pair.
            A malformed surrogate pair will raise a UnicodeEncodeError.

            Setting ucs4 True turns surrogate pair decoding off, allowing access the full UCS-4 
            character range to a python interpreter built with four-byte Unicode 
            character support
            """

        Font.strength -> float
            """
            Amount by which font glyph's size is enlarged for strong or wide
            transformations, as a fraction of the untransformed size.

            A wide strength of 0.08333 (1/12) is equivalent to pygame.font.Font bold
            default is 1/36

            For wide, only the horizontal is increased
            For strong, both horizontal and vertical

            strength style is only supported for scalable fonts.
            setting this on a bitmap font AttributeError
            or font object is inactive --> RuntimeError
            """
        Font.underline_adjustment -> float
            """
            negative value turns an underline into a strike-through or overline
            Accepted value range between -2.0 and 2.0
            A value of 0.5 matches Tango underlining
            A value of 1.0 mimics pygame.font.Font underlining
            """
        Font.rotation -> int
            """
            baseline angle, default angle is 0, rotation value
            is normalized to range 0 to 359 inclusive

            Only scalable can be rotated
            """
        Font.fgColor -> Color

        Font.fixed_width -> bool  
            """
            READ ONLY

            If font contains fixed_width characters
            As:
                Courier
                Bitstream Vera Sans Mono
                Andale Mono
            """
        Font.fixed_sizes -> int 
            """ 
            READ ONLY
            
            Returns number of pointsize for which font contains bitmap
            character images. if zero then not a bitmap font.
            """
        Font.scalable -> bool # READONLY Like the 2 above
class pygame.cursors:
    __doc__:
        """
        Pygame offers control over system hardware cursor
        Only support black and white cursors for the system
        Can control cursor with functions inside pygame.mouse

        Cursors module contains functions for loading and decoding
        various cursor formats. Also several standard cursors
        
        The pygame.mouse.set_cursor() function takes several arguments
        All those arguments have been stored in a single tuple you can call like:
            >>> pygame.mouse.set_cursor(*pygame.cursors.arrow)

        Also contains a few cursors as formatted strings. need to 
        pass them to pygame.cursors.compile() before using them
            >>> cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
            >>> pygame.mouse.set_cursor(*cursor)
        ---
        Cursor bitmaps that can be used as cursor:
            pygame.cursors.arrow
            pygame.cursors.diamond
            pygame.cursors.broken_x
            pygame.cursors.tri_left
            pygame.cursors.tri_right
        Following strings can be converted into cursor bitmaps
            pygame.cursors.thickarrow_strings
            pygame.cursors.sizer_x_strings
            pygame.cursors.sizer_y_strings
            pygame.cursors.sizer_xy_strings
        ---
        """
    cursors.compile(strings, black='X', white='.', xor='o') -> data, mask
        """
        Create binary cursor data from sequence of strings

        Width of the strings must all be equal and divisble by 8

        xor color (system color) sets a special toggle for it.
        If system does not support xor cursors, color will simply be black
        """
    cursors.load_xbm(cursorfile) -> cursor_args
    cursors.load_xbm(cursorfile, maskfile) -> cursor_args
        """
        XBM files are traditionally used to store cursors on UNIX. 
            They are an ASCII format to represent simple images

       Sometimes black and white color values will be split into 2 separate XBM
       you can pass a second maskfile  argument to loa two images into a single

       cursorfile and maskfile can either be
        - filenames
        - file-like object with readlines method
       """

class pygame.display:
    __doc__:
        """
        pygame has a single display Surface that is
            - Windowed
            - Fullscreen

        Once you create the display, you treat it as a regular Surface
        Changes are not imediately visible onscreen, need to flip/update

        By default the display is a basic software driven framebuffer
        Can request special modules like hardware acceleration and OpenGL suppport

        Creating a new one with pygame.display.set_mode() will close prevdisplay

        If precise control is needed over pixel format or display resolutions use:
            pygame.display.mode_ok()
            pygame.display.list_modes()
            pygame.display.Info()

        Once display Surface is created, functions from module affect it
            Surface becomes invalid if module is unitialized

        When display mode is set, several events are placed on event queue
            pygame.QUIT when user requests program to shutdown
            pygame.ACTIVEEVENT events as display gains and loses focus
            pygame.VIDEORESIZE if display is set with pygame.RESIZABLE flag
            pygame.VIDEOEXPOSE (Hardware displays that draw direct to the screen)
                               (Will get this event when portions of window must be
                                redrawn)

        Some display environments have an option for automatically stretching
        all windows, when it is enabled, it distorts the appearance of the window
        In pygame examples directory, there is example code
        (prevent_display_stretching.py) which shows how to disable it on Windows
        """
    display.init() -> None
        """
        Pygame will select from one of several internal display backends
        Display mode will be chosen depending on platform and permissions
        Before display module is initalized, ennvironment variable 
        SDL_VIDEODRIVER can be set to control which backend is used
            Windows: windib, directx
            Unix: x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib

        On some platforms it is possible teo embed pygame display into 
        an already existing window. to do this 
        environment variable SDL_WINDOWID must be set to a string containing
        window id or handle. Be aware there can be many strange side effects
        """
    display.get_init()  -> bool   
    display.quit() -> None    
        """
        Any active displays will be closed
        """
    display.set_mode((size=(0, 0), flags=0, depth=0, display=0)) -> Surface
        """ 
        Initialize a window or screen for display.
        Arguments are "requests", while actual created display is best match.

        size --> (width, height)
        depth --> number of bits to use for color

        If size == (0, 0) and pygame uses SDL 1.2.10+
            same size as current screen resolution
            If only width or height is set to 0
                same width or height as screen resolution

        It is usually best to not pass depth.
            It will default to best and fastest color depth
        If game requires a specific color format, can control depth
            Pygame will emulate an unvailable color depth, can be slow

        When requesting fullscreen, sometimes exact match cannot be made.
            Return surface will always match requested size though

        On high resolution displays and tiny graphics games, show up very small.
            SCALED scales up the window for you. game still thinks it is a 
            640x480? window, but everything is scaled, including mouse events.

        you can combine multiple types of flags using bitwise or operator (|)
        There are several to choose form:
            pygame.FULLSCREEN
            pygame.DOUBLEBUF (Recommended for HWSURFACE or OPENGL)
            pygame.HWSURFACE (Hardware accelerated, only in FULLSCREEN)
            pygame.OPENGL (OPENGL-renderable display)
            pygame.NOFRAME (no border or controls)
            pygame.SCALED (resolution depends on desktop size and scale graphics)

        pygame.SCALED is python 2.0.0+    

        display index 0 means that default display is used
        """

    display.flip() -> None
        """
        If using HWSURFACE and DOUBLEBUF
            will wait for a vertical retrace and swap surfaces

        Elif using pygame.OPENGL:
            perform a gl buffer swap

        Else: Simply update entire contents of surface
        """
    display.update(rectangle=None) -> None
    display.update(rectangle_list) -> None       
        """
        optimized version that allows only a portion to be updated
        (if no rectangle is passed it updates entire area)

        You can pass a single rectangle or a sequence of rectangles
        More efficient to pass many rectangles at once than calling multiple
        If passing a sequence of rectangles it is safe to include None values

        This call cannot be used on pygame.OPENGL displays (Exception)
        """
    display.get_surface() -> Surface

    display.set_icon(Surface) -> None
        """
        Can pass any surface, but most systems
        want a smaller image around 32x32.

        Image can have colorkey transparency which will be passed to system

        Some systems do not allow window icon to change after it has been shown.
        So, this function can be called before set_mode then
        """
    display.set_caption(title, icontitle=None) -> None
        """
        Some systems support an alternate shorter title to be used on minimized
        displays.
        """
    display.get_caption() -> title, icontitle # often title==icontitle
    display.get_window_size() -> tuple
        """
        Is different from size of display surface if SCALED is used

        return the size of the actual window
        """

    display.get_active() --> bool
    display.iconify() --> bool
        """
        Iconify the display surface
        Not all systems and display support iconified display

        Return True if successful
        """

    display.get_driver() -> name
    display.Info() -> VideoInfo
        """
        A simple object containing several attributes

        If this is called before set_mode, some platforms
        can provide information about default display mode.

        Can also be called after set_mode to verify specific display options

        hw --> True if hardard accelerated
        wm --> True if windowed display modes can be used
        video_mem --> MBs of video memory on display, 0 if unknown
        bitsize --> Number of bits per pixel
        bytesize --> Number of bytes per pixel
        masks --> four values used to pack RGBA values into pixels
        shifts --> four values uses to pack RGBA values into pixels
        losses --> four values used to pack RGBA values into pixels
        blit_hw --> True if hardware Surface blitting is accelerated
        blit_hw_CC --> True if hardware Surface colorkey blitting is accelerated
        blit_hw_A --> True if hardware Surface pixel alpha blitting is accelerated
        blit_sw --> True if software Surface blitting is accelerated
        blit_sw_CC
        blit_sw_A
        current_h, current_w: Height and width of current video mode 
                              (or of desktop mode if called before set_mode)
        """
    display.get_wm_info() -> dict
        """
        Get information about current windowing system

        Creates a dictionary filled with string keys.
        The strings and values are arbitrary created by the system.

        Most platforms will return a window key 
            with value set to system id for current display
        """
    display.list_modes(depth=0, flags=pygame.FULLSCREEN, display=0) -> list
        """
        List of possible sizes for a specific color depth
        return value will be empty if no display modes are available
        -1 means that any size would work (likely case for windowed modes)
        Mode sizes are sorted from biggest to smallest

        If depth is 0, SDL will choose the current/best color depth
        
        flags deafult to pygame.FULLSCREEN, but you may need to add additional
        flags for specific fullscreen modes

        display index 0 means the default display is used
        """
    display.mode_ok(size, flags=0, depth=0, display=0) -> depth
        """
        Use same arguments as set_mode, used to determine if requested mode is 
        available. if it is, return a pixel depth that best matches. else return
        0 if display mode cannot be set.

        Usually depth argument is not passed, but some platforms can support 
        multiple display depths, if passed, it will hint to which depth is a
        better match.

        most useful flags to pass will be
        HWSURFACE, DOUBLEBUF and maybe FULLSCREEN
        """
    pygame.display.get_num_displays() -> int # Always 1 with sdl < 2.0.0

    display.gl.get_attribute(flag) -> value
        """
        Get value for an OpenGL flag for current display         
        
        After calling set_mode with OPENGL flag. It is a good idea to check
        value of any requested OpenGL attributes.
        """
    display.gl.set_attribute(flag, value) -> None    
        """
        After calling pygame.display.set_mode with OPENGL flag. 
        Pygame automatically handles OpenGL attributes like color and 
        double-buffering. 

        The OPENGL flags are:
            - GL_MULTISAMPLEBUFFERS --> Whether to enable multisampling anti-aliasing
                Defaults to 0
                Set to a value above 0 to control amount of AA (typically 2-3)
            - GL_STENCIL_SIZE --> Minimum bit size for stencil buffer (Default 0)
            - GL_DEPTH_SIZE --> Minimum bit size for depth buffer (Default 16)
            - GL_STEREO --> 1 enables stereo 3D. (Default 0)
            - GL_BUFFER_SIZE --> Minimum bit size of frame buffer (Default 0)
            - GL_MULTISAMPLESAMPLES
            - GL_ACCUM_RED_SIZE
            - GL_ACCUM_GREEN_SIZE
            - GL_ACCUM_BLUE_SIZE
            - GL_ACCUM_ALPHA_SIZE

        New in pygame 2.0
            - GL_ACCELERATED_VISUAL --> 1 to require hardware acceleration
                                        0 to force system render (Default:Both)
            - GL_CONTEXT_PROFILE_MASK --> Set OpenGL profile to a value of:
                - GL_CONTEXT_PROFILE_CORE: disable deprecated features
                - GL_CONTEXT_PROFILE_COMPATIBILITY: allow deprecated features
                - GL_CONTEXT_PROFILE_ES: Allow only the ES feature subset of OpenGL
            - GL_CONTEXT_MAJOR_VERSION
            - GL_CONTEXT_MINOR_VERSION
            - GL_CONTEXT_FLAGS
            - GL_SHARE_WITH_CURRENT_CONTEXT
            - GL_CONTEXT_RELEASE_BEHAVIOR
            - GL_FRAMEBUFFER_SRGB_CAPABLE                                         
        """
 
    display.toggle_full_screen() --> bool
        """
        Only works with UNIX X11 video driver

        For most situations it is better to call set_mode
        
        Switches between fullscreen and windowed
        """

    display.set_palette(palette=None) -> None
        """ 
        Change video display color palette for 8-bit displays
        Will not change the palette for the actual display Surface
        only the palette that is used to display the surface

        If no palette argument is passed, system default palette will be restored

        The palette is a sequence of RGB triplets
        """
    display.set_gamma(red, green=None, Blue=None) -> bool
        """
        Set red, green and blue gamma values on display hardware
        if green and blue are not passed --> same as red

        Not all systems and hardware support gamma ramps

        Return True if succeeded

        1.0 gamma --> linear color table
        Lower values --> darken
        Higher --> brighten
        """
    display.set_gamma_ramp(red, green, blue) -> bool
        """
        Change hardware gamma ramps with a custom lookup

        Each argument should be sequence of 256 integers
        integers should range between 0 and 0xffff

        Not all systems and hardware support gamma ramps
        Return True if succeeded
        """
class pygame.draw:
    __doc__:
        """
        Rendering to hardware surfaces will be slower than software surfaces.

        Most take a width argument to represent the thickness, if 0: filled.
            if width < 0 --> nothing will be drawn
        Color arguments can be
            - A pygame.Color
            - An RGB/RGBA
            - Integer value that has been mapped to surface's pixel format
                (See pygame.Surface.map_rgb() and pygame.Surface.unmap_rgb())

        color's alpha value will be written directly into the surface. But draw 
        function will not draw transparently.

        These functions temporarily lock the surface they are operating on.

        Also see pygame.gfxdraw for alternative draw methods
        """
    pygame.draw.rect(surface, color, rect, width=0) -> Rect
        """
        Note: On using width values > 1. Edge lines will grow outside boundary

        Note: pygame.Surface.fill() works just as well for filled rects.
        Can be hardare accelerated on some platforms with both software and
        hardware display modes.
        """
    pygame.draw.polygon(surface, color, points, width=0) ->  Rect
        """
        Return a rect bounding changed pixels.
        If nothing is drawn, the rect position will be the position
        of first point in points parameter.

        ValueError if len(points) < 3
        TypeError if points not a sequence

        For an aapolygon, use aalines() with closed=True
        """
    pygame.draw.circle(surface, color, center, radius, width=0) -> Rect
        """
        center can be tuple or list or Vector2

        When using width values > 1, edge lines will only grow inward.
        """
    pygame.draw.ellipse(surface, color, rect, width=0) -> Rect
    
    pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1) -> Rect
        """
        Draw an elliptical arc on given surface

        angles are given in radians (float) and indicate the
        start and stop positions, counterclockwise direction

        if start_angle > stop_angle:
            stop_angle += tau (2*pi)

        width <= 0--> nothing will be drawn   

        width values > 1, edge lines grow inward from original boundary
        """
    pygame.draw.line(surface, color, start_pos, end_pos, width=1) -> Rect
        """
        start_pos and end_pos are tuples,lists or Vector2

        width < 1 --> nothing will be drawn

        For odd width values, thickness of each line grows
        with original line being in center

        For even width values, thickness grows with original line
        being offset from the centers
        As a result:
            - Lines with slope < 1 (horizontal-ish)
                will have one more pixel of thickness below original line
            - Lines with slope > 1
                will have one more pixel to the right
        """
    pygame.draw.lines(surface, color, closed, points, width=1) -> Rect
        """
        closed --> an additional line segment is drawn between first and last 

        Drawing thick lines with sharp corners can have undesired looking effects
        """
    pygame.draw.aaline(surface, color, start_pos, end_pos, blend=1) -> Rect    
        """
        if non-zero, line will be blended with surface's existing pixel shades
        Otherwise, overwrite them
        """
    pygame.draw.aalines(surface, color, closed, points, blend=1) -> Rect
class pygame.gfxdraw:
    __doc__:
        """
        EXPERIMENTAL

        (EXPERIMENTAL FOR LONG TIME NOW
        A BIT SLOWER, HAS MORE OPTIONS)

        Draw several shapes to a surface.
        For all functions, the arguments are strictly positional
        Only integers are accepted for coordinates and radii


        For functions like Rectangle any (x, y, w, h) is accepted. 
        Though pygame.Rect instances are preferred.
        The drawing will not include Rect.bottomright as they lie one 
        pixel outside of Rect's border.

        To draw an aa and filled shape, first use aa version then use
        filled version.

        You need to import pygame.gfxdraw before using it

        EACH of the functions releases the GIL during the C part of the call.

        pygame.gfxdraw module differs from draw module in the API it uses
        and different functions available to draw. It also wraps the
        primitives from SDL_gfx rather than using modified versions
        """

    gfxdraw.pixel(surface, x, y, color) -> None
    gfxdraw.hline(surface, x1, x2, y, color) -> None
    gfxdraw.vline(surface, x, y1, y2, color) -> None
    gfxdraw.line(surface, x1, y1, x2, y2, color) -> None
    gfxdraw.arc(surface, x, y, r, start, end, color) -> None

    gfxdraw.rectangle(surface, rect, color) -> None
        """
        Draw rectangle EDGES onto a surface
        Surface.fill() works just as well.
        In fact it can be hardware accelerated on some
        platforms with both software and hardware display modes
        """
    gfxdraw.box(surface, rect, color) -> None 
    gfxdraw.circle(surface, x, y, r, color) -> None
    gfxdraw.aacircle(surface, x, y, r, color) -> None
    gfxdraw.filled_circle(surface, x, y, r, color) -> None
    gfxdraw.ellipse(surface, x, y, rx, ry, color) -> None
    gfxdraw.aaellipse(surface, x, y, rx, ry, color) -> None
    gfxdraw.filled_ellipse(surface, x, y, rx, ry, color) -> None
    gfxdraw.trigon(surface, x1, y1, x2, y2, x3, y3, color) -> None #triangle
    gfxdraw.aatrigon(surface, x1, y1, x2, y2, x3, y3, color) -> None #triangle
    gfxdraw.filled_trigon(surface, x1, y1, x2, y2, x3, y3, color) -> None #triangle
    gfxdraw.polygon(surface, points, color) -> None
    gfxdraw.aapolygon(surface, points, color) -> None
    gfxdraw.filled_polygon(surface, points, color) -> None



    gfxdraw.pie(surface, x, y, r, start, end, color) -> None
    gfxdraw.textured_polygon(surface, points, texture, tx, ty) -> None
        """
        A per-pixel alpha texture blit to a per-pixel alpha surface
        will differ from a Surface.blit() blit

        Also a per-pixel alpha texture cannot be used with an 8-bit
        per pixel destination
        """
    gfxdraw.bezier(surface, points, steps, color) -> None
class pygame.image:
    """
    loading/saving images

    transferring Surfaces to formats usable by other packages

    There is no image class, an image is loaded as a Surface object

    By default it only loads uncompressed BMP images.

    When built with full image support, pygame.image.load()
    can support:
        JPG
        PNG
        GIF (non-animated)
        BMP
        PCX
        TGA (uncompressed)
        TIF
        LBM (and PBM)
        PBM (and PGM, PPM)
        XPM

    Saving images only supports  a limited set:
        BMP
        TGA
        PNG
        JPEG
    """
    image.load(filename) -> Surface
    image.load(fileobj, namehint='') -> Surface
        """
        If you pass a raw file-like object
        you may also want to pass original filename
        as namehint argument (mainly for extension?)

        returned Surface will contain same color format, colorkey and
        alpha transparency.

        You will often want to call Surface.convert() with no arguments
        to create a copy that will draw more quickly on the screen.

        For alpha transparency like in .pg images, use the
        convert_alpha() method after loading so that the image has
        per pixel transparency.

        you should use os.path.join() for compatibility
        """               
    image.save(Surface, filename) -> None  
    image.get_extended() -> bool # If extended image formats can be loaded

    image.tostring(Surface, format, flipped=False) -> string
        """
        Can be transferred with 'fronstring' in other
        Python imaging packages,
        some image packages prefer them flipped like PyOpenGL

        format argument can be:
            - P (8-bit Pallettized)
            - RGB 
            - RGBX (32-bit image with unused space)
            - RGBA
            - ARGB
            - RGBA_PREMULT (colors scaled by alpha channel)
            - ARGB_PREMULT
        
        other Python image packages support more formats than pygame.
        """
    image.fromstring(string, size, format, flipped=False) -> Surface
        """
        size argument is pair of numbers for width and height
        Once new Surface is created, can destroy string buffer.
        """
    image.frombuffer(string, size, format) -> Surface
        """
        Shares pixel data directly from string buffer
        Can't flip source data
        Much faster than fromstring
        """
class pygame.Surface:
    Surface((width, height), flags=0, depth=0, masks=None) -> Surface
    Surface((width, height), flags=0, Surface) -> Surface
        """
        Surfaces with 8-bit pixels use a color palette to map to 24-bit color.
        With no additional arguments, will choose format best matching.

        pixel format controlled by passing bit depth or existing Surface.
        flags argument is a bitmask of additional features, you can
        pass any combination of:
            HWSURFACE -> Creates the image in video memory
            SRCALPHA -> pixel format will include a per-pixel alpha.
        both flags are only a request. and may not be possible for all 
        display and formats.

        (for more complete set of flags, maybe check get_flags()) 

        Advance users can combine a set of bitmasks wwith a depth value.
        The masks are a set of 4 integers representing which bits in a pixel
        will reprsent each color.

        Surfaces can have many extra attributes like alpha planes, colorkeys,
        source rectangle clipping. these functions mainly effect how Surface
        is blitted. The blit routines will attempt to use hardware acceleration
        when possible else highly optimized software blitting methods.
        --
        There are three types of transparency supported in pygame:
            colorkeys - surface alphas - pixel alphas.
        Surface alphas can be mixed with colorkeys, but pixel alphas
        cannot use other modes.

        Colorkey transparency makes a single color value transparent.
        Any pixels matching colorkey will not be drawn.

        Surface alpha value is a single value that changes transparency
        for entire image. 255 is opaque surface, 0 is completely transparent.

        Per pixel alphas store a transparency value for every pixel. This
        allows ofr most precise but also the slowest.
        --
        There is support for pixel access for Surfaces using get_at() and set_at()
        They are fine for simple access, but are consierably slow when
        doing a lot of pixel work with them. So it is recommended to use
        PixelArray instead, which gives an array-like view of the surface.
        For involved mathematical manipulations, try pygame.surfarray method
        (Quite quick! but requires Numpy)

        Any function that directly access a surface's pixel data will
        need to lock() that surface. these function can lock() and unlock()
        the surface themselves, but if it is called too many times. there
        will be an overhead. so it is best to lock surface manually then
        unlock when finished.
        Remember to leave surface locked only when necessary.

        Surface pixels are stored internally as a single number, use map_rgb()
        and unmap_rgb() to convert.

        Each Surface contains a clipping area, By default, the clip area 
        covers the entire Surface. if it is changed, all drawing operations will 
        only effect the smaller area.
        """

    Surface.blit(source, dest, area=None, special_flags=0) -> Rect
        """
        Dest can either be a pair of coordinates
        representing upperleft corner, or a Rect.

        Size of dest does not effect hte blit.

        An optional area Rect can be passed, this represents
        a smaller protion of source Surface to draw.

        special_flags:
            BLEND_ADD
            BLEND_SUB
            BLEND_MULT
            BLEND_MIN
            BLEND_MAX

            BLEND_RGBA_ADD
            BLEND_RGBA_SUB
            BLEND_RGBA_MULT
            BLEND_RGBA_MIN
            BLEND_RGBA_MAX
            # Repeated for BLEND_RGB_xxx  
        
        Pixel alphas will be ignored when blitting to an 8bit Surface.
        For a surface with colorkey or blanket alpha, a blit to self may 
        give slightly different colors.
        """# areas changed.
    Surface.blits(blit_sequence=((source, dest), ...), doreturn=1) -> [Rect, ...] or None
    Surface.blits((source, dest, area), ...) -> [Rect, ...]
    Surface.blits((source, dest, area, special_flags), ... ) -> [Rect, ...]
    Surface.fill(color, rect=None, special_flags=0) -> Rect
        """
        Alpha value is ignored unless usrface uses perpixel alpha
        special_flags are same as those in blit
        """
    
    Surface.convert(Surface=None) -> Surface
    Surface.convert(depth, flags=0) -> Surface
    Surface.convert(masks, flags=0) -> Surface
        """
        No arguments --> same pixel format AS SET_MODE, always fastest format
        for blitting, it is a good idea to convert all Surfaces
        before they are blitted many times.

        Converted surface will have no pixel alphas. They 
        will be stripped if original had them
        (See convert_alpha() for preserving or creating 
        per-pixel alphas.)

        New copy will have same class, so can inherit without
        overriding, unless subclass specific instance attributes
        need copying.
        """
    Surface.convert_alpha(Surface) -> Surface
    Surface.convert_alpha() -> Surface
        """
        Change the pixel format of an image including
        per pixel alphas.

        New surface will be in a format suited for quick blitting
        to the given format with per pixel alpha.

        If no surface is given, the new surface will be
        optimized for blitting to the current dispaly.

        Unlike convert() method, pixel format will not exactly
        be the same as 'requested' source, but it will be optimized
        for fast alpha blitting.

        Also, same class, like convert()
        """
    Surface.copy() -> Surface # same Pixel, Palettes, Transparency, Class.

    Surface.set_colorkey(Color, flags=0) -> None
    Surface.set_colorkey(None) -> None
        """
        Set current colorkey for Surface,
        when blitting this Surface into any destination,
        any points that have the same color as
        the colorkey will be transparent.

        color can be an RGB or a mapped color integer. If None,
        colorkey will be unset.

        colorkey will be ignored if using per pixxel alpha values.
        can be mixed with full alpha values.

        optional flags argument can be set to
        pygame.RLEACCEL to provide better performance on non-accerlated
        displays, slower to modify but quicker to blit.
        """
    Surface.get_colorkey() -> RGB or None
    Surface.set_alpha(value, flags=0) -> None
    Surface.set_alpha(None) -> None
        """
        Set alpha value for the full Surface image,
        when blitting onto a desstination, pixels will be
        drawn slightly transparent, from 0 to 255.

        If None is passed, then alpha blending will be
        disabled, including per-pixel ealpha.

        For a surface with per-pixel alpha, blanket alpha
        is ignored and None is returned.
    
        Can use pygame.RLEACCEL as a flag.
        pygame 2.0:
        per-surface alpha can be combined with per-pixel alpha.

        """
    Surface.get_alpha() -> int_value
   

    Surface.lock() -> None
        """
        On accerelated Surfaces, the pixel data may be stored in
        volatile video memory or nonlinear comprssed forms. When a 
        Surface is locked, pixel memory becomes available to access by
        regular software. Code that reads or writes pixel values will
        need the Surface to be locked.

        Surfaces should not remain locked for more than necessary. A locked
        Surface can often not be displayed or managed by pygame.

        Not all Surfaces require locking, the mustlock() method
        can determine if it is actually required. There is no
        performance penalty for locking and unlocking a Surface
        that does not need it.

        IT is safe to nest locking and unlocking calls.
        The surface will only be unlocked after final lock is released
        """
    Surface.unlock() -> None
    Surface.mustlock() -> bool
        """
        Usually pure software Surfaces do not require locking,
        this method is rarely needed, since it is safe and quickest
        to just lock all Surfaces as needed.
        """
    Surface.get_locked() -> bool    
    Surface.get_locks() -> tuple

    Surface.get_palette() -> [RGB, RGB, RGB, ...]
        """
        Returned list is a copy of the palette,
        changes will have no effect.
        """    
    Surface.get_palette_at(index) -> RGB
    Surface.set_palette([RGB, RGB, RGB, ...]) -> None
        """
        A partial palette can be passed, and only
        the first colors will be changed.

        has no effect on Surface with more than 8bits per pixel
        """
    Surface.set_palette_at(index, RGB) -> None
    #
    Surface.get_at((x, y)) -> Color
        """
        Get a copy of the RGBA Color value, if no per-pixel alpha
        then it will always be 255.

        Will temporarily lock and unlock the Surface as needed
        """
    Surface.set_at((x, y), Color) -> none
    
    Surface.scroll(dx=0, dy=0) -> None
        """
        Move image by dx pixels right and dy pixels down.
        May be negative for left and up scrolls.

        Scrolling is contained by Surface clip areas.
        It is safe to have dx, dy exceeding Surface size.
        """
    Surface.set_clip(rect) -> None
    Surface.set_clip(None) -> None
    Surface.get_clip() -> Rect
    Surface.get_bounding_rect(min_alpha = 1) -> Rect
        """
        Enveloping all pixels that have
        an alpha value greater than or equal
        min_alpha
        """

    Surface.subsurface(Rect) -> Surface
        """
        Shares pixels with new parent
        Considered a child or original
        Modifications to either will efect each other!
        Surface information like clipping area and
        color keys are unique to each Surface.

        Will inherit palette, colorkey and any alpha settings
        from parent.

        Possible to have any number of subsurfaces
        and subsubsurfaces onthe parent, also to
        subsurface the display surface if display mode is not
        hardware aceclererated

        See get_offset() and get_parent() to learn more about
        state of subsurface

        A subsurface will have same class as parent
        """    
    Surface.get_parent() -> Surface # Else return None 
    Surface.get_abs_parent() -> # Top level, Else return self
    Surface.get_offset() -> (x, y) # position of child inside a parent or (0, 0)
    Surface.get_abs_offset() -> (x, y) # Else return (0, 0)

    Surface.map_rgb(Color) -> mapped_int
        """
        Returned integer will contain no more bits than the bit
        depth of te Surface.

        Mapped color values are not used inside pygame, but
        can be passed to most functions that require a Surface and a
        color.
        """
    Surface.unmap_rgb(mapped_int) -> Color

    Surface.get_size() -> (width, height)
    Surface.get_width() -> width
    Surface.get_height() -> height
    Surface.get_rect(**kwargs) -> Rect
        """
        Rect starts at (0, 0) topleft
        kwargs will be applied to attributes of Rect
        before it is returned
        example:
        mysurf.get_rect(center=(100, 100))
        """
    Surface.get_bitsize() -> int
    Surface.get_bytesize() -> int
    Surface.get_flags() -> int
        """
        SWSURFACE -> Surface is in system memory
        HWSURFACE -> Surface is in video memory
        ASYNCBLIT -> Use Asynchorous blits if possible

        Available for set_mode():

        ANYFORMAT -> Allow any video depth/pixel-format
        HWPALETTE -> Surface has exclusive palette
        FULLSCREEN
        OPENGL
        RESIZABLE
        NOFRAME

        Used Internally:

        HWACCEL -> Blit uses hardware acc.
        SRCCOLORKEY -> Blit uses source colorkey
        RLEACCELOK -> Private flag
        RLEACCEL -> Surface is RLE encoded
        SRCALPHA -> Blit uses source alpha blending
        PREALLOC -> Surface uses preallocated memory.
        """         
    Surface.get_pitch() -> int
        """
        Get number of bytes separating each row in the Surface

        Surfaces in video memory are not always linearly packed.
        Subsurfaces will also have a larger pitch than their real width.

        This value is not needed for normal pygame usage
        """ # Not needed normally
    Surface.get_masks() -> (R, G, B, A)
        """
        The bitmasks needed to convert between a color and
        a mapped integer

        Not needed for normal pygame usage
        """# Not needed normally
    Surface.get_shifts() -> (R, G, B, A) # Not needed normally
    Surface.get_losses() -> (R, G, B, A) # Not needed normally
        """
        Return least significant number of bits
        stripped from each color in a mapped integer
        """

    Surface.set_masks((r, g, b, a))  -> None # Not needed normally
    Surface.set_shifts((r, g, b, a)) -> None # Not needed normally

    
    Surface.get_view(<kind>='2') -> BufferProxy
        """
        Return an object which exports a surface's
        internal pixel buffer as a level array struct,
        python level array interface or a C level buffer
        interface. It is writeable.

        Kind argument is the length 1 string
        '0', '1', '2', '3', 'r', 'g', 'b' or 'a'
        Letters are case insensitive

        '0' -> contiguous unstructured bytes view. No surface
        shape information is given. A valueError is raised if
        surface's pixels re discontinuous.

        '1' -> A (surface-width * surface-height) array of contguous
        pixels. ValueError if discontinuous

        '2' -> A (surface-width, surface-height) array of raw pixels.
        They are surface-bytesize-d unsigned integers. Pixel format
        is surface specific. The 3-byte unsigned integers of 24-bit
        surfaces are unlikely accepted by anything other than other
        pygame functions.

        '3' -> A (surface-width, surface-height, 3) array of RGB
        color components, each of the red, green and blue components
        are unsigned bytes. Only 24-bit and 32-bit surfaces are supported.
        Must be either RGB or BGR orden within the pixel.

        'r'/'g'/'b'/'a' return a (Surface-width, surface-height) view
        of a single color component within a surface: a color plane.
        Color components are unsinged bytes. both 24-bit and 32-bit support
        'rgb'. Only 32-bit with SRCALPHA support 'a'

        The surface is locked only when an exposed interface is accessed
        For new buffer interface accesses, the surface is unlocked once
        the last buffer view is released. While for array interface
        and old buffer interface accesses, the surface remains locked
        until BufferProxy object is released
        """
    Surface.get_buffer() -> BufferProxy
        """
        Return a buffer object for pixels of Surface.
        The buffer can be used for direct pixel access and
        manipulation. 
        Surface pixel data is represented as an
        unstructured block of memory, with a start address and
        length in bytes.
        Data need not to be continuous, any gaps are included in the length
        but otherwise ignored.

        This method implicitly locks the Surface, and unlocks when
        BufferProxy is grabage collected.
        """

     Surface._pixels_address -> int # Starting address of surface's raw pixel bytes



class pygame.mask:
    __doc__:
        """
        Useful for fast pixel perfect collision detection.
        A mask uses 1 bit per pixel to store which parts collide
        """

    pygame.mask.from_surface(Surface, threshold=127) -> Mask
        """
        Creates a Mask object out of the given surface by setting all opaque 
        pixels and not transparent pixels.

       If the surface uses a color-key, then it is decided which bits in the
       resulting mask are set. All pixels that are not equal to color-key are set
       and vice versa.

       If color-key is not used. then the alpha value of each pixel is used
       to decide which bits in the resulting mask are set. All pixels having
       an alpha value greater than the threshold parameter are set, vice versa.
       """ 
    pygame.mask.from_threshold(surface, color, threshold=(0, 0, 0, 255),
                            othersurface=None, palette_colors=1) -> Mask
        """
        More featureful method.

        If optional othersurface is not used, all pixels within threshold
        of color parameter are set in resulting mask.

        Else, all pixels in the first surface that is within the threshold of
        corresponding pixel in othersurface is set in the resulting mask.

        Surface --> Surface to create the mask from
        Color --> Ignored if othersurface is given
        threshold --> threshold range to check difference between 2 colors.
        othersurface --> used to check whether the pixel of first surface are
                        within the threshold of pixels from this surface
        palette_colors -> indicates whether to use the palette colors or not.
        """

    class Mask:
        Mask(size=(width, height), fill=False) -> Mask
            """
            Used to represent a 2d bitmask, each bit represents a pixel.
            1 is used to indicate a set bit and 0 for unset bit.
            Set bits in a mask can be used to detect collisions with other masks
            and their set bits.

            A filled mask has all of its bits set to 1, conversely an unfilled/
            cleared/empty masks has all bits set to 0.
            Masks can be created unfilled or filled by using fill parameter
            or  by using Mask.clear() and Mask.fill()

            A mask coordinates start in topleft corner at (0, 0) and 
            individual bits can be accessed by Mask.get_at() and Mask.set_at()

            The methods overlap(), overlap_area(), overlap_mask(), draw(), 
            erase() and convolve() use an offset parameter to indicate the 
            offset of another mask's top left corner from calling mask's 
            top left corner. THe calling mask's top left corner is origin.
            Offsets are a tuple or list of 2 integer values.

            
            In pygame 2.0.0: Subclassing support and shallow copying added.
            """


        Mask.get_size() -> (width, height)
        Mask.get_at((x, y)) -> int
        Mask.set_at((x, y), value=1) -> None

        Mask.count() -> bits # number of set bits
        Mask.centroid() -> (x, y)
        Mask.angle() -> theta 
            """
            Finds approximate orientation from -90 to 90 degrees
            of set bits in the mask. works best if only one
            connected component
            """
        Mask.outline(every=1) -> [(x, y), ...]
            """
            Return list of points of outline of first connected component
            encountered, searched per row strting in topleft corner.

            "every" optional parameter skips set bits in outline, so every=10
            returns a list of every 10th set bit in outline.
            """


        Mask.fill() -> None
        Mask.clear() -> None
        Mask.invert() -> None
        Mask.draw(othermask, offset) -> None # bitwise OR, drawing othermask into this
        Mask.erase(othermask, offset) -> None # Erase all bits set in othermask from this


        Mask.overlap(othermask, offset) -> (x, y)
            """
            return first point of intersection, 2 overlapping set bits.

            searches overlapping area in sizeof(unsigned long int) * CHAR_BIT
            bit wide column blocks. For clarity it will be referred to be as W

            (0, 0) to (W - 1, 0) then
            (0, 1) to (W - 1, 1) and so on.
            """
        Mask.overlap_area(othermask, offset) -> numbits 
            """
            Can be useful for collision detection,
            an approximate collison normal can be found by
            calculating gradient of overlapping area through the finite 
            difference.

            >>> dx = mask.overlap_area(othermask, (x+1, y)) -
                     mask.overlap_area(othermask, (x-1, y))
            >>> dy = mask.overlap_area(othermask, (x, y+1)) - 
                     mask.overlap_area(othermask, (x, y-1))
            """
        Mask.overlap_mask(othermask, offset) -> Mask

        Mask.scale((width, height)) -> Mask
        Mask.convolve(othermask, outputmask=None, offset=(0, 0)) -> Mask
            """
            Returns a Mask with (i - offset[0], j - offset[1]) bit set, if shifting
            other mask (such that its bottom right corner is at (i, j)) causes

            it to overlap with this mask.

            If an output mask is specified, the output is drawn onto it and it
            is returned. Otherwise a mask of size
            (MAX(0, width+othermask's width - 1), MAX(0, height+othermasks' height -1))
            is created and  returned
            """
        Mask.connected_component() -> Mask
        Mask.connected_component((x, y)) -> Mask
            """
            A connected component is a group (1 or more) of connected
            set bits (orthogonally and diagonally). The SAUF algorithm
            which checks 8 point connectivity is used.

            By default this method will return a Mask containing largest
            connected component in the mask, optionaally a bit coordinated
            can be specified and the connected component containing it
            will be returned. If the bit at the given location is not set
            returned Mask will be empty
            """
        Mask.connected_components(min=0) -> [Mask, ...] #min=0 is equiv. to min=1  
        Mask.get_bounding_rects() -> [Rect, ...] # for all connected comp.

        # pygame 2+
        Mask.copy() # same width, height and set/unset bibts
        Mask.get_rect(**kwargs) -> Rect #i.e. a_mask.get_rect(center=(10, 5))
        Mask.to_surface(surface=None, setsurface=None, unsetsurface=None,
                        setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 255)) -> Surface
            """
            Return a surface with mask drawn on it

            surface -> Optional surface to draw mask onto.
                       if None:
                        create a surface with size same as mask.
                        flags = SRCALPHA
                        depth = 32
                        to be created, drawn on and returned.

            setsurface -> Use this surface's color values to draw
                          set bits if surface is smaller than the mask
                          any bits outside use setcolor value.

            rest is self-explonatory

            use None for setcolor/unsetcolor to skip drawing them.
            also setsurface/unsetsurface take precedence over
            those parameters
            """                                 
class pygame.Rect:
    __doc__:
        """
        attributes are:
            Rect.x
            Rect.y
            Rect.top
            Rect.left
            Rect.bottom
            Rect.right
            Rect.topleft
            Rect.bottomleft
            Rect.topright
            Rect.bottomright
            Rect.midtop
            Rect.midleft
            Rect.midbottom
            Rect.midright

            Rect.center
            Rect.centery
            Rect.cerx
            Rect.size
            Rect.height
            Rect.width
            Rect.w
            Rect.h
        
        all assignments change other attributes

        Coordinates are all integers
        Size values can have negative values, but are illegal
        for most operaetions.

        If a rect has a nonzero width/height it will return True for a non-zero test

        The area covered by a Rect does not include the right- and bottom-most
        edge of pixels. If one Rect's bottom border is another's top border, the two
        meet exactly on screen but do not overlap.

        Rect class can be subclassed, copy() and move() will recognize
        this and return instances of subclass. However, __init__() method
        of subclass is not called and __new__ is assumed to take no arguments.
        So these methods should be overriden if any extra attributes need
        to be copied.
        """
    
    Rect.copy() -> Rect
    Rect.move(x, y) -> Rect #offset
    Rect.move_ip(x, y) -> None
    Rect.inflate(x, y) -> Rect
        """
        Size changed by given offset
        rectangle remains centered around its current center

        Negative values will shrink the rectangle.

        If offset is too small, center will be off  -2<x<2
        """
    Rect.inflate_ip(x, y) -> None
    
    Rect.clamp(Rect) -> Rect 
        """
        Return a new Rect that is moved to be
        completely inside the argument Rect, if too large
        to fit, then it is centered inside.
        """
    Rect.clamp_ip(Rect) -> None
    Rect.clip(Rect) -> Rect
        """
        Return a new rectangle that is cropped
        to be completely inside argument Rect,
        if two rectangles do not overlap to begin with
        A rect with size 0 is returned
        """
    Rect.union(Rect) -> Rect
    Rect.union_ip(Rect) -> None
    Rect.unionall(Rect_sequence) -> Rect
    Rect.unionall_ip(Rect_sequence) -> None
    Rect.fit(Rect) -> Rect
        """
        Return a new rectangle that is moved and resized to fit
        another. The aspect ratio of original Rect is preserved.
        """

    Rect.normalize() -> None # correct negative sizes

    Rect.contains(Rect) -> bool # completely inside
    Rect.collidepoint((x, y)) -> bool
    Rect.collidepoint(x, y) -> bool
    Rect.colliderect(Rect) -> bool # overlap
    Rect.collidelist(Rect_list) -> index # return first index, -1 if no match
    Rect.collidelistall(Rect_list) -> indices # return [] if no match
    Rect.collidedict(dict, use_values=0) -> (key, value) or None
        """
        Return the first key and value pair that intersects
        with calling Rect object. if no collisions are found.
        None is returned

        If use_values == 0 --> use keys in collison detection
        else use dict's values

        Note: 
        Rect objects cannot be used as keys, so they must
        be converted to a tuple/list

        tuple(key_rect) 
        """
    Rect.collidedictall(dict, use_values) -> [(key, value), ...]
class pygame.sprite:
    __doc__:
        """
        These classes are fairly lightweight and only provide a starting
        place for the code that is common to most games.

        The basic Sprite class is intended to be used as a base class for
        the different types of objects in the game. 
        There's also a base Group class that simply stores sprites.
        A game could create new types of Group classes that operate on specially
        customized Sprite instances they contain.

        The basic Sprite class can draw the Sprites it contains to a Surface.
        The Group.draw() method requires that each Sprite have a Surface.image
        attribute and a Surfuace.rect. The Group.clear() method requires these
        attributes and can be used to erase all the Sprites with background. There
        are also more advanced Groups:
            pygame.sprite.RenderUpdates()
            pygame.sprite.OrderedUpdates()

        Lately, it contains several collision functions, these help find sprites
        inside multiple groups that have intersecting bounding rectangles. To find
        the collisions, the Sprites are required to have a Surface.rect attribute
        assigned.

        The groups are designed for high efficiency in removing and adding Sprites
        to them. They also allow cheap testing to see if a Sprite already exists in a
        Group. A given Sprite can exist in any number of groups. A game
        could use some groups to control object rendering, and a completely
        separate set of groups to control interaction or player movement. Instead of
        adding type attributes or bools to a derived Sprite class. Consider keeping
        the Sprites inside Organized Groups. This will allow for easier lookup later.

        Sprites and Groups manage their relationships with add() and remove()
        methods. It is safe to repeatedly add and remove the same Sprite from a GRroup.

        Sprites are not thread safe. So lock them yourself if using threads.
        """

    class Sprite:
        Sprite(*groups) -> Sprite  
            """
            The base class for visible game objects.
            Derived classes will want to override the
            Sprite.update() and assign a Sprite.image and Sprite.rect
            attributes.

            When subclassing the Sprite, be sure to call base initializer before
            adding the Sprite to Groups. For example:
            """
                class Block(pygame.sprite.Sprite):
                    def __init__(self, color, width, height):
                        pygame.sprite.Sprite.__init__(self)

                        self.image = pygame.Surface([width, height])
                        self.image.fill(color)
                        # Could also be an iamge loaded from disk.

                        self.rect = self.image.get_rect()
                        # Update position of this object, by updating rect.x, rect.y

        Sprite.update(*args) -> None
            """
            does nothing, just a convenient hook that you can
            override. This method is called by Group.update()
            with whatever arguments you give it.

            No reason to use this if not using the convenient
            method by same name in Group class.
            """
        
        Sprite.add(*groups) -> None
            """
            Any number of Group instances be be passed as arguments.
            The Sprite will be added to the Groups it is not already a member of.
            """
        Sprite.remove(*groups) -> None        
        Sprite.kill() -> None # ONLY remove the Sprite from all Groups
        Sprite.alive() -> bool # does the sprite belong to any groups
        Sprite.groups()
    class DirtySprite(Sprite):
        """ A subclass of Sprite with more attributes and features"""
        DirtySprite(*groups) -> DirtySprite   

        DirtySprite.dirty = 1
            """
            1 -> Repainted and then set to 0 again
            0 -> not dirty, therefore not repainted again.
            2 -> always dirty, repainted each frame. flag is not reset.
            """
        DirtySprite.blendmode = 0 # special_flags argument of blit
        DirtySprite.source_rect = None 
            """
            Source rect to use, it is relative to topleft of self.image
            """
        DirtySprite.visible = 1
            """
            Normally 1, if set to 0 it will not be repainted.
            (You must set it dirty too to be erased from screen)
            """
        DirtySprite.layer = 0 # READONLY VALUE, only used with LayeredDirty            

    class Group:
        Group(*sprites) -> Group
            """
            A container class to hold and manage multiple Sprite objects.
           
            This class can be inherited to create contains with more
            specific behaviors. The group supports:

            in 
            len
            bool
            iter

            The sprites are not ordered, so drawing and iterating the
            Sprites is in no particular order 
            """
        Group.copy() -> Group
            """
            Creates a new Group with same Sprites

            If you have subclassed Group.
            The new object will have same subclass as original.
            This will only work if derived's class construcot
            has same arguments as the Group class's
            """
        
        Group.update(*args) -> None
            """
            Call update method on contained Sprites
            
            args will be passed to each Sprite

            No way to get return value from the Sprite.update() methods
            """


        Group.sprites() -> sprite_list
        Group.empty() -> None # Remove all Sprites
        Group.add(*sprites) -> None
        Group.remove(*sprites) -> None
        Group.has(*sprites) -> None # if it contains ALL of the given sprites
        # From the above functions, Each sprite argument can also be an iterator
        # containing Sprites


        Group.draw(Surface) -> None # blit the Sprite images
        Group.clear(Surface_dest, background) -> None 
            """
            Erases the Sprites used in the Group.draw() call
            by filling drawn Sprites positions with the background.

            background is usually a Surface image the same dimensions
            as the destination Surface

            It can also be a callback function that takes two arguments,
            the destination Surface, and an area to clear.
            It will be called several times each clear.
            Example:
            """
                def clear_callback(surf, rect):
                    color = 255, 0, 0
                    surf.fill(color, rect)
    class RenderUpdates(Group):
        RenderUpdates.draw(surface) -> Rect_list
            """
            Also return a list of rectangular areas
            on the screen that has been changed.

            Include changes by previous Group.clear() calls

            Returned Rect list should be passed to pygame.display.update()
            To help perforamnce on software driven display mode.
            Usually only helpful on destinations with non-animating backgrounds.
            """
    class OrderedUpdates(RenderUpdates):
        # Draws Sprites in order of addition
        # Maintains order in wihch Sprites were added for rendering
        # Makes adding and removing Sprites a little slower.
    class GroupSingle(Group):
        GroupSingle(sprite=None) -> GroupSingle
            """
            Only holds a single sprite, when a new sprite
            is added, the old one is removed.

            There is a special property
            Groupsingle.sprite that access the Sprite
            that this Group contains (or None)

            Can also be set to add a Sprite into it
            """

    class LayeredUpdates():
        LayeredUpdates(*sprites, **kwargs) -> LayeredUpdates
            """
            A group that handles layers and draws like OrderedUpdates

            Fully compatible with sprite.Sprite

            Can set default layer through kwargs using
            'default_layer' and an integer, the default_layer is 0

            If the sprite you add has an attribute layer, then that layer
            will be used. If the **kwarg contains 'layer' then the 
            sprites passed will be added to that layer (overriding the
            sprite.layer attribute). If neither, then default layer is used
            """

        LayeredUpdates.add(*sprites, **kwags) -> None
        LayeredUpdates.sprites() -> sprites # ordered list, first back, last top
        LayeredUpdates.get_sprites_at(pos) -> colliding_sprites
        LayeredUpdates.get_sprite(idx) -> sprite 

        LayeredUpdates.get_layer_of_sprite(sprite) -> layer
        LayeredUpdates.get_sprites_from_later(layer) -> sprites # ordered by how they were added, linear search.
        LayeredUpdates.remove_sprites_of_layer(layer_nr) -> list of sprites
        LayeredUpdates.layers() -> layers # unique, sorted from bottom up
        LayeredUpdates.change_layer(sprite, new_layer) -> None
        LayeredUpdates.switch_layer(layer1_nr, layer2_nr) -> None # Switch sprites from layer 1 to layer 2


        LayeredUpdates.get_top_layer() -> layer
        LayeredUpdates.get_bottom_layer() -> layer
        LayeredUpdates.move_to_front(sprite) -> None # added to end of topmost layer
        LayeredUpdates.move_to_back(sprite) -> None 
        LayeredUpdates.get_top_sprite() -> Sprite


        LayeredUpdates.draw(surface) -> Rect_list
    class LayeredDirty(LayeredUpdates):
        LayeredDirty(*sprites, **kwargs):
            """
            For DirtySprite Objects, Subclasses LayeredUpdates

            Requires pygame.sprite.DirtySprite of any
            sprite that has the following attributes:

            image, rect, dirty, visible, blendmode

            Uses the dirty flag technique, therefore faster than
            pygame.sprite.RenderUpdates if you have many static sprites.
            Also switches automatically between dirty rect update and
            full screen drawing, so you don't have to worry what would be faster.
            
            You can specify some additional attributes through kwargs

            _use_update: True/False
            _default_layer
            _time_threshold: threshold time for switching between
                             dirty rect mode and full screen mode,
                             defaults to 1000./80 == 1000./fps

                             # 1000. for float
            """                 

        LayeredDirty.draw(surface, bgd=None) -> Rect_list
            """
            Draw all sprites in the right order onto
            passed surface, you can pass the background too
            """
        LayeredDirty.clear(surface, bg) -> None
        LayeredDirty.repaint_rect(screen_rect) -> None    

        LayeredDirty.set_clip(screen_rect=None) -> None
            """
            clip the area where to draw
            Just pass None to reset the clip
            """
        LayeredDirty.get_clip() -> Rect
        
        LayeredDirty.change_layer(sprite, new_layer) -> None

        LayeredDirty.set_timing_treshold(time_ms) -> None # typo in name :/


    sprite.spritecollide(Sprite, group, dokill, collided=None) -> Sprite_list
        """
        Find sprites in a group that intersect another sprite
        (By comparing Sprite.rect of each Sprite)

        if dokill: remove all sprites from that group.

        Collided argument is a callback function used
        to calculate if two sprites are colliding, it should
        take two sprites as values and return a bool value.
        If collided is not passed, all sprites must have a
        "rect" value
        """
    sprite.collide_rect(left, right) -> bool
        """
        Tests for collision between two sprites,
        Uses pygame rect colliderect function to calc.
        the collision. Intended to be passed as a collided
        callback function to the collide functions.

        Sprites must have a "rect" attribute for this
        """
    sprite.collide_rect_ratio(ratio) -> collided_callable
        """
        A callable class that checks for collisions
        between 2 sprites using a scaled version.

        Is created with a ratio, then the instance
        is passed as a collided callback

        1.0 is same size, 2.0 is twice as big and 0.5 is half size
        """
    sprite.collide_circle(left, right) -> bool
        """
        Tests for collision between two sprites.
        By checking if two circles centered on sprites overlap.

        sprites must have a "rect" attribute and
        an optional "radius" attribute
        Otherwise a circle is created that is big enough
        to completely enclose the sprites rects

        """
    sprite.collide_circle_ratio(ratio) -> collided_callable
    sprite.collide_mask(left, right) -> point
        """
        Return first point on the mask where masks collided
        or None if no collision.

        Tests for collision between two sprites, by testing
        if their bitmasks overlap. If the sprites have a mask
        attribute, that is used as a mask, otherwise a mask is created
        from the sprite image.

        This is intended to be passed as a collided callback function to
        the collide functions. Sprites must have a 'rect' attribute and
        an optional 'mask'

        You should consider creating a mask for your sprite at load time
        if you are going to check collisions many times

        sprite.mask = pygame.mask.from_surface(sprite.image)
        """

    sprite.groupcollide(group1, group2, dokill1, dokill2, collided=None) -> sprite_dict
        """
        Will find collisions between all sprites in two groups.

        Every Sprite inside group1 is added to return dictionary.
        Value for each item is list of sprites in group2 that
        intersect.
        """
    sprite.spritecollideany(sprite, group, collided=None) -> Sprite or None # quicker
class pygame.transform:
    __doc__:
        """
        A surface is transform is an operation that moves
        or resizes the pixels. All these functions take a Surface
        to operate on and return a new Surface withe results.

        Some are destructive (lose pixel data each time preformed)
        For this reason, it is better to re-transform the original
        surface than to keep transforming an image multiple times
        (Like resizing and rotating)
        """

    transform.flip(Surface, xbool, ybool) -> Surface # Non-destructive
    transform.scale(Surface, (width, height), DestSurface=None) -> Surface
        """
        Resizes to a new resolution
        Fast scale operation that doesn't sample the results   

        Giving a DestSurface is quicker if you want to repeatedly scale something
        However it must be same size passed in and same format
        """
    transform.rotate(Surface, angle) -> Surface 
        """
        Unless "flipping":
        Image will be padded larger to hold new size,
        If image has pixel alphas, padded area will be transparent.
        Otherwise pygame willp ick color that matches Surface colorkey
        or topleft pixel value
        """
    transform.rotozoom(Surface, angle, scale) -> filtered 32-bit Surface
        """
        Scale then rotate? TBD
        """
    
    transform.scale2x(Surface, DestSurface=None) -> Surface
        """
        Uses advanceMAME Scale2X algorithm which does a 'jaggie-less' scale
        of bitmap graphics.

        Only has an effect on simple images with solid colors, on photographic
        and AA images it will look like a regular unfiltered scale.
        """
    transform.smoothscale(Surface, (width, height), DestSurface=None) -> Surface
        """
        Uses one of two different algorithms for scaling each
        dimension as required.

        For shrinkage: The output pixels are area averages of the colors
        they cover.
        For expansion: A blinear filter is used.

        For the x86-64 and i686 architectures, optimized MMX routines
        are included and will run much faster than other machine types.

        This will only work for 24-bit or 32-bit surfaces
        """    
    transform.get_smoothscale_backend() -> String # Used for debugging and testing.
        """
        Shows whether or not smoothscale is using MMX or SSE acc.

        If no acceleration is available then 'GENERIC' is returned.
        
        The level of acceleration to use for a x86 processor is determined
        at runtime.
        """
    transform.set_smoothscale_backend(type) -> None
    
    transform.chop(Surface, rect) -> Surface
        """
        Extracts a portion of an image, all vertical and
        horizontal pixels surrounding given rectangle area are removed.

        THe corner areas (diagonal to the rect) are then brought together.
        (Original image is not altered btw)    

        Note: If you want a 'crop' that returns part of an image within a rect
        you can blit with a rect to a new surface or copy a subsurface.
        """
    transform.laplacian(Surface, DestSurface=None) -> Surface
        """
        Find edges in a surface using laplacian algorithm
        """
    
    transform.average_surfaces(Surfaces, DestSurface=None, palette_colors=True) -> Surface
        """
        Takes a sequence of surfaces and returns a surface with
        average colors from each of the surfacers

        palette_colors - if True, we average colors in palette,
        otherwise we average pixel values. Useful if surface
        is actually greyscale colors and not palette colors.

        Note: This function does not handle palette-using surfaces correctly""" 
    transform.average_color(Surface, Rect = None) -> Color 
        """
        Find average color of a Surface or a region
        """

    
    transfom.threshold(dest_surf, surf, search_color, threshold=(0,0,0,0),
        set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set = False) -> num_threshold_pixels
        """
        This versatile function can be used to find colors in a 'surf'
        close to a 'search_color' or close to colors in a separate 'search_surf'

        It can also be used to transfer pixels into a 'dest_surf' that 
        match or don't match.
        By default it sets pixels in 'dest_surf' where rall of the pixels NOT
        within the threshold are changed to set_color. If inverse_set
        is optionally set to True, then pixels that ARE within the threshold
        are cange.


        dest_surf can be None if just counting.
        threshold as in "within the distance"

        set_behavior = 0 -> we do not change dest_surf, just count
        set_behavior = 2 -> pixels set in 'dest_surf' will be from 'surf'
        """

class pygame.PixelArray:
    __doc__:
        """
        It wraps a Surface and provides direct access to its pixels
        Can be one or two dimensional.
        Support slicing, for returning a subarray or for assignment.
        A pixel rray sliced on a single column or row returns a one dimensional
        A pixel array can be safely assigned to itself.

        They export an array struct interface, allowing them to interact
        with pygame.pixelcopy and Numpy arrays.

        Pixarray pixel item can be assigned a raw integer value, a pygame.Color instance or tuple
        However only a pixel's integer value is returned.
        So must be mapped first using Surface.map_rgb() of the Surface
        object for which pixelarray was created
        >>>   if pxarray[0, 0] == surface.map_rgb((0, 0, 255))


        When assigning to a range of pixels, can use a sequence or even a pixArray

        If right hand side array has a row length of 1, then columns is broadcast
        over target array's rowws. An array of height 1 is broadcast over 
        target's columns and is equivalent to assigning a 1D PixelArray

        >>> newarray = pxarray[2:4, 3:5]
        >>> otherarray = pxarray[::2, ::2] # subscript slices, rectangular subview

        CAn also be used to do fast rectangular pixel manipulations
        instead of iterating over x or y axis.:
        >>> pxarray[::2, :] = (0, 0, 0) # Make even columns black
        >>> [::2] = (0, 0, 0) # same as [::2, :]

        PixArray locks surface, so you have to close() it once it is done.
        It is best to use it as a context manager:

        with PixelArray(surf) as pixel_array: 
            style()

        
        A note about PixelArray to PixelArray assignemnts, for arrays with an item
        size of 3 (24 bit surfaces). Pixel values are translated from source
        to destination format. RGB of each pixel are shifted to match format of
        target surface, for all other pixel sizes. No such remapping occurs. This
        should change in later pygame releases, where format conversions are performed 
        for all pixel Size. To avoid code breakagle, it is suggested that PixelArray
        to PixelArray copies be only between surfaces of identical format.
        """
    PixelArray.surface -> Surface
    PixelArray.itemsize -> int #bytesize
    PixelArray.ndim -> int # number of dimensions
    PixelArray.shape -> tuple of ints # tuple of ndims
    PixelArray.strides -> tuple of ints # tuple of Byte offsets for dimension, -ve means inverted

    PixelArray.make_surface() -> Surface
    # sf = pxarray[:, ::-1].make_surface() # flipped surface
    PixelArray.replace(color, repcolor, distance=0, weights=(0.299, 0.587, 0.114)) -> None
        """
        Uses a simple weighted euclidean distance formula to calc. distance
        between colors. distance space ranges from 0.0 to 1.0 and used
        as threshold for color detection. this causes replacement 
        to take pixels with a similar but not exactly identical color into
        account as well

        in place operation.
        """     
    PixelArray.extract(color, distance=0, weights=(0.299, 0.587, 0.114)) -> PixelArray
        """
        Change all matching pixels to white, while non-matching to black
        """
    PixelArray.compare(array, distance, weights=(0.299, 0.587, 0.114)) -> PixelArray
    
    PixelArray.transpose() -> PixelArray # If 1-D returns a 2-D

    PixelArray.close()
class pygame.pixelcopy:
    __doc__:
        """
        functions for copying between surfaces and objects
        exporting an array structure interface.
        It is a backend for pygame.surfarray, adding Numpy
        support, but pixelcopy is more general, and intended for
        direct use.
        """
    pixelcopy.surface_to_array(array, surface, kind='P', opaque=255, clear=0) -> None
        """
        Copies pixels from a Surface object to a 2D or a 3D array.
        depending on argument kind and target array dimension,
        a copy may be raw pixel value, RGB, a color component size
        or a colorkey alpha transparency value.

        Recognized kind values are single chracter codes:
        'P' 'R ''G 'B' 'A' 'C' (case-insensitive)
        first two dimensions of target must be default size


        'P' -> direct raw integer pixel (mapped) value copy to a 2D array
        and a RGB pixel component (unmapped) copy to a 3D array having shape (w, h, 3)
        For an 8-bit colormap surface, table index copied to a 2D array
        not table value itself.
        A 2D array item's size must be at least as large as
        surface pixel byte size. while item size of a 3D array must be at least one byte.

        For the 'R', 'G', 'B', and 'A' copy kinds a single color component 
        of the unmapped surface pixels are copied to the target 2D array. 
        For kind 'A' and surfaces with source alpha (the surface was created 
        with the SRCALPHA flag), has a colorkey (set with Surface.set_colorkey())
        , or has a blanket alpha (set with Surface.set_alpha()) 
        then the alpha values are those expected for a SDL surface. 
        If a surface has no explicit alpha value,
        then the target array is filled with the value of the optional 
        opaque surface_to_array argument (default 255: not transparent). 

        'C' -> special case for alpha copy of a source surface with a colorkey
        unlike the 'A' colro component copy, the clear argument value is used for
        colorkey matches opaque otherwise. By default a match has alpha 0, while
        everything else is alpha 255. more general implementaiton of pygame.surfarray.array_colorkey()
        """
    pixelcopy.array_to_surface(<surface>, <array>) -> None # See pygame.surfarray.blit_array()
    pixelcopy.map_array(<array>, <array>, <surface>) -> None
    """
    map an array of color elements (w, h, .., 3) to an array
    of pixels (w, h) according to format of <surface>
    """
    pixelcopy.make_surface(array) -> Surface # Can be 2D or 3D 
class pygame.sndarray:
    __doc__:
        """
        convert between Numpy and Sound

        Sound data is made of thousands of samples per second
        and each sample is the amplitude of the wave
        at a particular moment in time.

        For example in 22-kHz format, element number 5
        of the array is the amplitude of the way after
        5/22000 seconds.

        Each sample is an 8bit or 16bit integer. depending on data format

        Stereo sound file has two values per sample. while a mono
        sound file only has one.
        """

    sndarray.array(Sound) -> array # copy Samples into an array
    sndarray.samples(Sound) -> array # references Samples into an array
    sndarray.make_sound(array) -> Sound 
class pygame.BufferProxy:
    __doc__:
        """
        pygame object to export a surface buffer through an array protocol
        BufferProxy(<parent>) -> BufferProxy

        BufferProxy is a pygame support type designed as
        return value of Surface.get_buffer() and Surface.get_view()

        For all python versions, a BufferProxy object exports
            - a C struct
            - a Python-level array interface
        For CPython 2.6+
            - A new buffer interface is also exported

        BufferProxy is key to implementing pygame.surfarray module
        ---
        BufferProxy instances can be created directly from Python code
            1. either for a parent that exports an interface
            2. or from a python dict describing object's buffer layout
                the following keys are recognized:
                "shape": tuple
                    length of each array dimension as tuple of integers
                    length of tuple is number of dimensions
                "typestr": 3-string
                    array element type as a length 3 string
                        first char: "<" little-endian
                                    ">" big-endian
                                    "|" non applicable
                        second char: "i" signed integer
                                     "u" unsigned integer
                                     "f" floating point
                                     "V" for a chunk of bytes
                        third char: bytesize of element from '1' to '9' 
                    example: "<u4" unsigned 4 byte little endian integer
                    such as a 32 bit pixel on a PC
                        "|V3" a 24 bit pixel, has no integer equivalent  
                "data": 2-tuple
                    1. physical buffer start address (int)  
                    2. read-only flag (bool)
                "strides": tuple (optional)
                    Array stride information as a tuple of integers
                    It is required only of non C-contiguous arrays
                    Tuple length must match that of "shape
                "parent": object (optional)
                    Exporting object. Can be used to keep parent object alive while
                    its buffer is visible.
                "before": callable (optional)
                    Callback invoked when BufferProxy instance exports the Buffer
                        callback is given one argument:
                            "parent" object if given else None
                        useful for setting a lock on parent
                "after": callable (optional)
                    When exported buffer is released
                    same as "before" but useful for releasing a lock instead
        ---
        It supports subclassing, instance variables and weak references
        (weak references are not counted by python's garbage collector)
        """
    BufferProxy.parent -> <parent> #(or Surface) 
        # Return wrapped exporting object
        # Surface which reeturned BufferProxy object or object passed to
        # BufferProxy call
    BufferProxy.length -> int
        # Size in bytes of exported buffer
    BufferProxy.raw -> bytes
        # copy of exported buffer as single block of bytes
    BufferProxy.write(buffer, offset=0):
        """
        Overwrite Bytes in parent object data. Must be C or F contiguous
            ValueErorr
        Argument buffer is a str/ bytes object.
        Optional offset gives a start position in bytes within buffer
            If negative or grater than or equal to buffer length 
                IndexException
            If len(buffer) > proxy.length + offset
                ValueError    
        """
class pygame.surfarray:
    __doc__:
        """
        Every pixel is stored as a single integer value to represent the RGB colors.
        The 8-bit images use a value that looks into a colormap.
        Pixels with higher depth use a bit packing process to place 3/4 values into a single number.

        Arrays re indexed by X-axis first then Y-axis. rrays that treat pixels
        as a single integer are referred to as 2D arrays.
        This module can also separate the red, green and blue color values
        into separate indices, referred to as 3D arrays. 
        """

    surfarray.array2d(Surface) -> array
        """
        Copy mapped (raw) pixels from a Surface into a 2d array.
        The bit depth of the surface will control the size of the integer
        values and will work for any type of pixel format.

        Temporarily locks Surface as pixels re copied
        """    
    surfarray.pixels2d(Surface) -> array
        """
        directly references pixel values, any changes will affect pixels.

        FAST operation since no data is copie.

        24-bit Surface cannot be referenced.

        Will remain locked for lifetime of array
        """# doesn't work for 24-bit
    surfarray.array3d(Surface) -> array
    surfarray.pixels3d(Surface) -> array # only works for 24/32-bit surfaces
    surfarray.array_alpha(Surface) -> array
        """
        Copy pixel alpha values from a Surface into a 2D array.
        Will work for any type of Surface format.

        Surface without a pixel alph will return array with all opaque values.

        As alway,s lock Surface as pixels are copied.
        """
    surfarray.pixels_alpha(Surface) -> Array # only on 32-bit with per-pixel alpha    
    surfarray.pixels_red(Surface) -> Array # only works for 24/32-bit surfaces
    surfarray.pixels_green(Surface) -> Array # only works for 24/32-bit surfaces
    surfarray.pixels_blue(Surface) -> Array # only works for 24/32-bit surfaces
    surfarray.array_colorkey(Surface) -> Array 
        """
        Create a new array with colorkey transparency value
        from each pixel. If pixel matches colorkey it will be 
        fully transparent, otherwise it will be fully opaque.

        Will work on any type of surface format. Also locks surface
        while copying.
        """

    surfarray.make_surface(array) -> Surface    
        """
        Uses array struct interface to acquire array properties,
        so not just limited to numpy arrays.
        (See  pygame.pixelcopy)

        Create a new surface that best ensembles data and format.
        Array can be 2D or 3D with any sized integer values
        """
    
    surfarray.blit_array(Surface, array) -> None
        """
        Directly copy values from an array into a Surface.
        This is faster than converting the array into a Surface
        and blitting. 

        Array must be same dimension as Surface and
        will completely replace all pixel values. 
        Only integer ASCII Characters and record arrays are accepted.

        Locks surface as values are copied
        """
    surfarray.map_array(Surface, array3d) -> array2d
        """
        Will use given Surface format to control the conversion.

        Palette Surface formats are supported for numpy arrays
        """


class pygame.key:
    __doc__:
        """
        event queue gets pygame.KEYDOWN and pygame.KEYUP
        Both events have a key attribute, integer ID representing key

        pygame.KEYDOWN has two additional attributes
            - unicode: single character string, fully translated character
                taking into account shift and compositon keys
            - scancode: platform-specific key code, could be different from
                keyboard to keyboard, but could be useful for key selection
                of weird keys like multimedia keys.
        NEW in pygame 2.0:
            pygame.TEXTINPUT is preferred to unicode attribute of pygame.KEYDOWN
            attribute text contains input.

        keyboard constants:
            KeyASCII      ASCII   Common Name
            K_BACKSPACE   \b      backspace
            K_TAB         \t      tab
            K_CLEAR               clear
            K_RETURN      \r      return
            K_PAUSE               pause
            K_ESCAPE      ^[      escape
            K_SPACE               space
            K_EXCLAIM     !       exclaim
            K_QUOTEDBL    "       quotedbl
            K_HASH        #       hash
            K_DOLLAR      $       dollar
            K_AMPERSAND   &       ampersand
            K_QUOTE               quote
            K_LEFTPAREN   (       left parenthesis
            K_RIGHTPAREN  )       right parenthesis
            K_ASTERISK    *       asterisk
            K_PLUS        +       plus sign
            K_COMMA       ,       comma
            K_MINUS       -       minus sign
            K_PERIOD      .       period
            K_SLASH       /       forward slash
            K_0           0       0
            K_1           1       1
            K_2           2       2
            K_3           3       3
            K_4           4       4
            K_5           5       5
            K_6           6       6
            K_7           7       7
            K_8           8       8
            K_9           9       9
            K_COLON       :       colon
            K_SEMICOLON   ;       semicolon
            K_LESS        <       less-than sign
            K_EQUALS      =       equals sign
            K_GREATER     >       greater-than sign
            K_QUESTION    ?       question mark
            K_AT          @       at
            K_LEFTBRACKET [       left bracket
            K_BACKSLASH   \       backslash
            K_RIGHTBRACKET ]      right bracket
            K_CARET       ^       caret
            K_UNDERSCORE  _       underscore
            K_BACKQUOTE   `       grave
            K_a           a       a
            K_b           b       b
            K_c           c       c
            K_d           d       d
            K_e           e       e
            K_f           f       f
            K_g           g       g
            K_h           h       h
            K_i           i       i
            K_j           j       j
            K_k           k       k
            K_l           l       l
            K_m           m       m
            K_n           n       n
            K_o           o       o
            K_p           p       p
            K_q           q       q
            K_r           r       r
            K_s           s       s
            K_t           t       t
            K_u           u       u
            K_v           v       v
            K_w           w       w
            K_x           x       x
            K_y           y       y
            K_z           z       z
            K_DELETE              delete
            K_KP0                 keypad 0
            K_KP1                 keypad 1
            K_KP2                 keypad 2
            K_KP3                 keypad 3
            K_KP4                 keypad 4
            K_KP5                 keypad 5
            K_KP6                 keypad 6
            K_KP7                 keypad 7
            K_KP8                 keypad 8
            K_KP9                 keypad 9
            K_KP_PERIOD   .       keypad period
            K_KP_DIVIDE   /       keypad divide
            K_KP_MULTIPLY *       keypad multiply
            K_KP_MINUS    -       keypad minus
            K_KP_PLUS     +       keypad plus
            K_KP_ENTER    \r      keypad enter
            K_KP_EQUALS   =       keypad equals
            K_UP                  up arrow
            K_DOWN                down arrow
            K_RIGHT               right arrow
            K_LEFT                left arrow
            K_INSERT              insert
            K_HOME                home
            K_END                 end
            K_PAGEUP              page up
            K_PAGEDOWN            page down
            K_F1                  F1
            K_F2                  F2
            K_F3                  F3
            K_F4                  F4
            K_F5                  F5
            K_F6                  F6
            K_F7                  F7
            K_F8                  F8
            K_F9                  F9
            K_F10                 F10
            K_F11                 F11
            K_F12                 F12
            K_F13                 F13
            K_F14                 F14
            K_F15                 F15
            K_NUMLOCK             numlock
            K_CAPSLOCK            capslock
            K_SCROLLOCK           scrollock
            K_RSHIFT              right shift
            K_LSHIFT              left shift
            K_RCTRL               right control
            K_LCTRL               left control
            K_RALT                right alt
            K_LALT                left alt
            K_RMETA               right meta
            K_LMETA               left meta
            K_LSUPER              left Windows key
            K_RSUPER              right Windows key
            K_MODE                mode shift
            K_HELP                help
            K_PRINT               print screen
            K_SYSREQ              sysrq
            K_BREAK               break
            K_MENU                menu
            K_POWER               power
            K_EURO                Euro                 

        keyboard also has a list of modifier states
        that can be assembled by bitwise-ORing them together
            KMOD_NONE
            KMOD_LSHIFT
            KMOD_RSHIFT
            KMOD_SHIFT

            KMOD_CAPS
            KMOD_LCTRL
            KMOD_RCTRL
            KMOD_CTRL

            KMOD_LALT
            KMOD_RALT
            KMOD_ALT
            KMOD_LMETA
            KMOD_RMETA
            KMOD_META
            KMOD_NUM
            KMOD_MODE
        """  
    key.get_focused() -> bool # If display window has keyboard focus
    key.get_pressed() -> bools 
        """
        Returns a sequence of boolean values state of every key on keyboard
        Use key constant values to index array.

        This is not proper ay to handle text entry from user.
        You have no way to know order of keys, and rapidly pushed keys can
        be completely unnoticed between two calls to pygame.key.get_pressed()

        See pygame.KEYDOWN for this functionality
        """
    
    key.get_mods() -> int
        """
        A single integer representing a bitmask of all mods being held"""
    key.set_mods(int) -> None
    
    key.set_repeat() -> None # Disabled
    key.set_repeat(delay, interval) -> None
    key.get_repeat() -> (delay, interval)
        """
        keys that are held down will
        generate multiple pygame.KEYDOWN events

        delay is number of ms before first
        after that interval will be sent every interval
        """


    key.name(key) -> string # descriptive name

    # New in pygame 2:
    key.start_text_input() -> None
        """
        Start receiving pygame.TEXTEDITING and pygame.TEXTINPUT events
        to handle IME

        A pygame.TEXTEDITING event is received when an IME 
        composition is started or changed. It contains
        the composition text, length and editing start position within
        the composition.

        When the composition is commited (or non-IME input is received)
        a pygame.TEXTINPUT event is generated
        """
    key.stop_text_input() -> None    
    key.set_text_input_rect(Rect) -> None
        """
        Control where the canddiate list will open, if supported.
        """
class pygame.mouse:
    __doc__:
        """
        when display mode is set, event queue will start receiving
        mouse events.
        button = 4 when wheel rolled up
        button = 5 when wheel rolled down

        pygame.MOUSEBUTTONDOWN and pygame.MOUSEBUTTONUP when
        presed and released. also mouse wheel does same when rolled.

        Whenever the mouse is moved, generates a pygame.MOUSEMOTION event
        Broken into small and accurate motion events.

        Primary reason that the event queue fills up.

        If mouse cursor is hidden and input is grabbed to the current display,
        the mouse will enter a virtual input mode, where the relative movements
        of the mouse will never be stopped by the borders of the screen
        see pygame.mouse.set_visible() and pygame.mouse.set_grab() to confgiure
        this.
        """

    mouse.get_pressed() -> (button1, button2, button3)
        """
        must call pygame.event.get() before this function
        else it will not work

        sequence of booleans representing the state
        of all mousebuttons
        """

    mouse.get_pos() # can be located outside of display window, but constrained to screen
    mouse.get_rel() -> (x, y) # since previous call to this funciton
    mouse.set_pos([x, y]) -> None
    
    mouse.set_visible(bool) -> bool # return previous visible state of cursor
    mouse.get_focused() -> bool    

    mouse.set_cursor(size, hotspot, xormasks, andmasks) -> None
        """
        size --> sequence containing width and height
        Hotspot --> sequence containing cursor hotspot position

        xormasks --> sequence of bytes containing xor data masks
        andmasks --> sequence of bytes containing cursor bitmask data

        Width must be a multiple of 8
        mask arrays must be correct size
        else an exception is raised
        """
    mouse.get_cursor() -> (size, hotspot, xormasks, andmasks)
    # new in pygame 2.0.0
    mouse.get_visible() -> bool

class pygame.scrap:
    __doc__:
        """
        EXPERIMENTAL

        dealing with clipboard, allows communication with other
        applications this way.

        Some basic data (MIME) types are defined and registered
            pygame constant ---> string value
            SCRAP_TEXT ---> 'text/plain'
            SCRAP_BMP ---> 'image/bmp'
            SCRAP_PBM ---> 'image/pbm'
            SCRAP_PPM ---> 'image/ppm'

        SCRAP_PPM, PBM and BMP are suitable for surface buffers
        to be shared with other applications.

        SCRAP_TEXT is an alias for the plain text clipboard type.

        For Window platforms, these additional types are supported automatically:
            "text/plain;charset=utf-8"
            "audio/wav"
            "image/tiff"

        Use defined types can be used, but the data might not be accessible
        by other applications unless they know what data type to look for.
        """        

    scrap.set_mode(mode) # only of interest for x11. Use pygame.SCRAP_CLIPBOARD
    scrap.init() -> None # requires set_mode first before init
    scrap.get_init() -> bool

    scrap.get(type) -> bytes or str or None
        """
        In python 3 the data is returned as a byte string and 
        might need further processing (such as decoding to unicode)

        ex. pygame.scrap.get(pygame.SCRAP_TEXT)   
        """
    scrap.get_types() -> list
    scrap.put(type, data) -> None # type can be a user defined
    scrap.contains(type) -> bool

    scrap.lost() -> bool # if clipboard ownership has been lost by pygame applciation
